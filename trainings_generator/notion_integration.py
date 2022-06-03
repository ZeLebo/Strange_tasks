from decouple import config
import requests as r
import datetime
import json


database_id = config("DATABASE_ID")
integration_token = config("ZHORA_TOKEN")

default_headers = {
    "Authorization": "Bearer " + integration_token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}


def create_page(list_exersice=None, tags=None, db_id=database_id, headers=None):
    if headers is None:
        headers = default_headers
    create_url = "https://api.notion.com/v1/pages"

    page_data = {
        "parent": {"database_id": db_id},
        "properties": {
            "Name": {
                # here need the template_mention_date
                "title": [
                    {
                        "type": "mention",
                        "mention": {
                            "type": "date",
                            "date": {
                                "start": datetime.datetime.now().strftime("%Y-%m-%d"),
                            }
                        }

                    }
                    # {
                    #     "text": {
                    #         "content": datetime.datetime.now().strftime("%m.%d.%Y")
                    #     }
                    # }
                ]
            },
            "Tags": {
                "multi_se lect": []
            }
        },
        "children": []
    }

    # adding tags
    if isinstance(tags, list):
        for i in tags:
            page_data["properties"]["Tags"]["multi_select"].append({"name": i})
    else:
        page_data["properties"]["Tags"]["multi_select"].append({"name": tags})

    # if many groups are added
    if isinstance(list_exersice, tuple):
        for i in range(min(len(list_exersice), len(tags))):
            # adding header
            data = {
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "text": {
                                "content": tags[i],
                                "link": None
                            }
                        },
                    ]
                }
            }
            page_data["children"].append(data)

            # adding exercises
            for exercise in list_exersice[i]:
                data_exercise = {
                    "type": "numbered_list_item",
                    "numbered_list_item": {
                        "rich_text": [
                            {
                                "text": {
                                    "content": exercise,
                                    "link": None
                                },
                            },
                        ],
                    },
                }
                page_data["children"].append(data_exercise)

    else:
        # adding headers
        data = {
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "text": {
                                "content": tags[0],
                                "link": None
                            }
                        },
                    ]
                }
            }
        page_data["children"].append(data)

        # adding exercises
        for i in list_exersice:
            data = {
                    "type": 'numbered_list_item',
                    "numbered_list_item": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": i,
                                    "link": None,
                                },
                            },
                        ],
                    },
                }

            page_data["children"].append(data)

    data = json.dumps(page_data)

    if (list_exersice is None) or (tags is None):
        print("Error: list_exersice or tags is None")
        return

    r.request("POST", create_url, headers=headers, data=data).json()


def main():
    create_page(["one", "two"], 'Back')


if __name__ == '__main__':
    main()
