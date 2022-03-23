// User, VM, code_pannel, terminal, controller

mtype : payment_status_enum = {INCORRECT_MONEY, CORRECT_MONEY, NO_MONEY};

chan UserCode = [1] of {bool};
chan Money = [1] of {mtype : payment_status_enum};
chan TerminalSignal = [1] of {bool};
chan UsGoAway = [1] of {bool};

proctype CodePannel() {
	do
		:: UserCode ? true ->
			TerminalSignal ! true;
		:: UserCode ? false -> UsGoAway ! false;
	od;
}

proctype Terminal(){
	// money putted?
	do
		:: TerminalSignal ? true;
		if
			:: Money ! INCORRECT_MONEY;
			:: Money ! CORRECT_MONEY;
			:: Money ! NO_MONEY;
		fi;
	od;
}

chan VM_Commands = [1] of {bool};

proctype Controller() {
	do
		:: mtype:payment_status_enum a;
			Money ? a;
			if
				:: a == INCORRECT_MONEY -> VM_Commands ! false;
				:: a == CORRECT_MONEY -> 
					VM_Commands ! true; // give tovar
				:: a == NO_MONEY -> VM_Commands ! false;
			fi;
	od;
}

proctype VM(){
	do
	:: VM_Commands ? true -> UsGoAway ! true;
	:: VM_Commands ? false -> UsGoAway ! false;
	od;
}


proctype User(){
	do
		:: short a = 0;
		do
			:: a < 20 -> a = a + 1;
			:: else -> break;
		od;
		if
			:: UserCode ! true;
			:: UserCode ! false;
		fi;
		do
			:: UsGoAway ? true -> break;
			:: UsGoAway ? false -> break;
		od;
	od;
}

init {
	atomic {
		run User();
		run Terminal();
		run CodePannel();
		run Controller();
		run VM();
	}
}


