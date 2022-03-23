mtype : water_temperature_status_enum = {EQUALS_1, EQUALS_2, EQUALS_3, NOT_PRESSED};
mtype : water_exist_status_enum = {EXIST, NOT_EXIST, POURED, NOT_POURED};
mtype : lid_status_enum = {IS_CLOSED, IS_OPENED, IS_LOCKED, IS_UNLOCKED};

chan userHere = [1] of {bool};
chan controllerCommand = [1] of {bool};
chan TP_command = [1] of {bool};
chan waterState = [1] of {mtype : water_exist_status_enum};
chan button = [1] of {mtype : water_temperature_status_enum};

proctype WaterChecker() {
    do
    :: userHere ? true;
    :: mtype:water_exist_status_enum a;
    waterState ? a;
    if 
    :: a == EXIST -> controllerCommand ! true;
    :: a == NOT_EXIST -> controllerCommand ! false;
    :: a == NOT_POURED -> controllerCommand ! false; 
    :: a == POURED -> controllerCommand ! true;
    fi
    od;
}


proctype Controller() {
    do
        :: controllerCommand ? true;
        if
            :: button ! EQUALS_1 -> TP_command ! true;
            :: button ! EQUALS_2 -> TP_command ! true;
            :: button ! EQUALS_3 -> TP_command ! true;
            :: button ! NOT_PRESSED -> TP_command ! false;
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