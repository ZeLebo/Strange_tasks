mtype: user_status_enum = {PRESS, PRESSED_SUCCESS};
mtype: lid_status_enum = {LOCK, UNLOCK, LOCKED, UNLOCKED};
mtype: heater_status_enum = {ON, ENDED, HEATER_ACCEPTED};


chan user_action_channel = [0] of { mtype:user_status_enum, byte };
chan lid_action_channel = [1] of {mtype: lid_status_enum, byte};
chan heater_action_channel = [1] of {mtype: heater_status_enum};

bool is_closed = true;
bool is_locked = false;
proctype User() {
    do
        ::      
            user_action_channel ! PRESS, 0;
            byte stat;
            user_action_channel ? PRESSED_SUCCESS, stat;
        :: is_locked == false -> is_closed = false;
        :: is_locked == false -> is_closed = true;
    od;
}

proctype Controller() {
    do
    ::  user_action_channel ? PRESS, 0 ->
        lid_action_channel ! LOCK, 0;
        byte ans;
        lid_action_channel ? LOCKED, ans;
        if
        :: ans == 1 ->
            heater_action_channel ! ON;
            heater_action_channel ? HEATER_ACCEPTED;
            user_action_channel ! PRESSED_SUCCESS, ans;
            heater_action_channel ? ENDED;
            heater_action_channel ! HEATER_ACCEPTED;
        :: else -> 
            user_action_channel ! PRESSED_SUCCESS, ans;
        fi;
    od;
}


proctype Lid(){
do
    :: lid_action_channel ? LOCK, 0 ->
        if
            :: is_closed == true ->
                atomic {
                    lid_action_channel ! LOCKED, 1;
                    is_locked = true;
                }
            :: else ->
            atomic {
                lid_action_channel ! LOCKED, 0;
                is_locked = false;
            }
        fi;
od;
}

bool is_heating = false;
proctype Heater() {
    do
        :: heater_action_channel ? ON ->
            atomic {
                is_heating = true;
                heater_action_channel ! HEATER_ACCEPTED;
            }
            :: is_heating == true ->
                atomic {
                    heater_action_channel ! ENDED;
                    is_heating = false;
                }
                heater_action_channel ? HEATER_ACCEPTED;
    od;
}

init {
    atomic {
        run User();
        run Controller();
        run Lid();
        run Heater();
    }
}

ltl p1 {[] (!(is_heating && !is_closed))}
ltl p2 {[](is_locked -> is_locked W is_heating)}
ltl p3 {[] (!(!is_closed && is_locked))}