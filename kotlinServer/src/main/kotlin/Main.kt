import com.sun.net.httpserver.HttpExchange
import com.sun.net.httpserver.HttpHandler
import com.sun.net.httpserver.HttpServer
import java.io.File
import java.net.InetSocketAddress

fun main(args: Array<String>) {
    // open a server on port 8000
    val server = HttpServer.create(InetSocketAddress(8000), 0)
    // define handlers
    server.createContext("/", DefaultHandler())
    server.createContext("/test", MyHandler())
    server.createContext("/files", FilesHandler())
    // start the server
    server.start()
}

// write from the html file
class DefaultHandler : HttpHandler {
    override fun handle(t: HttpExchange) {
        // check if request is GET
        if (t.requestMethod != "GET") {
            t.sendResponseHeaders(405, -1)
            return
        }
        // write prepared html file
        val response = File("./src/main/kotlin/prepared.html").readText()
        t.sendResponseHeaders(200, response.length.toLong())
        t.responseBody.write(response.toByteArray())
        t.responseBody.close()
    }
}

// test func
class MyHandler : HttpHandler {
    override fun handle(t: HttpExchange) {
        // check if request is GET
        if (t.requestMethod != "GET") {
            t.sendResponseHeaders(405, -1)
            return
        }
        // write test string to response
        val response = "This is the test handler"
        t.sendResponseHeaders(200, response.length.toLong())
        val os = t.responseBody
        os.write(response.toByteArray())
        os.close()
    }
}

class FilesHandler : HttpHandler {
    override fun handle(t : HttpExchange) {
        // check if request is GET
        if (t.requestMethod != "GET") {
            t.sendResponseHeaders(405, -1)
            return
        }
        // get the path from the request
        if (t.requestURI.query == null) {
            // print the files in the directory as links
            var response = File("./Files").listFiles()?.map {
                "<a href=\"/files?file=${it.name}\">${it.name}</a><br>"
            }?.joinToString("")
            if (response == null) {
                response = "No files found"
                t.sendResponseHeaders(404, 0)
                return
            }
            t.sendResponseHeaders(200, response.length.toLong())
            val os = t.responseBody
            os.write(response.toByteArray())
            os.close()
        } else {
            // get the file
            // parse file name from optional query
            val fileName = t.requestURI.getQuery().substring(5)
            // parse file name from query string
            val file = File("./Files/$fileName")
            if (file.exists()) {
                val response = file.readText()
                t.sendResponseHeaders(200, response.length.toLong())
                val os = t.responseBody
                os.write(response.toByteArray())
                os.close()
            } else {
                t.sendResponseHeaders(404, -1)
                t.responseBody.close()
            }
        }
    }
}
