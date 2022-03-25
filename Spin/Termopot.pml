mtype : water_temperature_status_enum = {EQUALS_1, EQUALS_2, EQUALS_3, NOT_PRESSED};
mtype : water_exist_status_enum = {EXIST, NOT_EXIST, POURED, NOT_POURED};
mtype : lid_status_enum = {IS_CLOSED, IS_OPENED, IS_LOCKED, IS_UNLOCKED};
mtype : button_status_enum = {PRESSED, RELEASED};

chan userHere = [1] of {bool};
chan TP_command = [1] of {bool};
chan controllerCommand = [1] of {bool};

chan lid = [1] of {mtype : lid_status_enum};
chan button = [1] of {mtype : button_status_enum};
chan waterState = [1] of {mtype : water_exist_status_enum};
chan temperature = [1] of {mtype : water_temperature_status_enum};

proctype WaterChecker() {
    do
    :: userHere ? true;
    :: mtype:water_exist_status_enum a;
    waterState ? a;
    if 
    :: a == EXIST && lid == IS_LOCKED && button-> controllerCommand ! true;
    :: a == NOT_EXIST -> controllerCommand ! false;
    :: a == NOT_POURED -> controllerCommand ! false; 
    :: a == POURED && lid == IS_LOCKED && button -> controllerCommand ! true;
    fi
    od;
}


proctype Controller() {
    do
        :: controllerCommand ? true;
        if
            :: temperature ! EQUALS_1 -> TP_command ! true;
            :: temperature ! EQUALS_2 -> TP_command ! true;
            :: temperature ! EQUALS_3 -> TP_command ! true;
            :: temperature ! NOT_PRESSED -> TP_command ! false;
        fi;
    od;
}

proctype TP() {
    do
    :: TP_command ! true -> userHere ! true;
    :: TP_command ! false -> userHere ! false;
    od;
}

proctype User() {
     do
    :: short a = 0;
    do
        :: a < 20 -> a = a + 1;
        :: else -> break
    od;
    do
        :: userHere ? true -> break;
        :: userHere ? false -> break;
    od;
    od
}


init {
    atomic {
        run User();
        run WaterChecker();
        run Controller();
        run TP();
    }
}

// If no water poured heating will not start
ltl p1 {[] (waterState[NOT_POURED]) == TP_command[false]};

// if lid is not locked the heating will not start
ltl p2 {[] (lid[IS_OPENED] || lid[IS_UNLOCKED]) == TP_command[false]};

// turning on after pressing the button
ltl p3 {[] (button[PRESSED] && waterState[POURED] && lid[IS_LOCKED]) == [] TP_command[true]};

// when the button is pressed the lid is locked
ltl p4 {[] button[PRESSED] == [] lid[IS_LOCKED]};

// the lid is closed till the end
ltl p5 {[] TP_command[true] == [] lid[IS_LOCKED]};