#TSensor and Output (0-2) Array Element Constants
TS_HLT =0
TS_MASH =1
TS_KETTLE =1
TS_H2OIN =3
TS_H2OOUT =4
TS_BEEROUT =5
TS_AUX1 =6
TS_AUX2 =7
TS_AUX3 =8
NUM_TS =9
BAD_TEMP =-32768


VS_MASH =1
VS_KETTLE =1

VS_PUMP =3

#Timers
TIMER_MASH =0
TIMER_BOIL =1

#Brew Steps
NUM_BREW_STEPS =16

STEP_FILL =0
STEP_DELAY =1
STEP_PREHEAT =2
STEP_ADDGRAIN =3
STEP_REFILL =4
STEP_DOUGHIN =5
STEP_ACID =6
STEP_PROTEIN =7
STEP_SACCH =8
STEP_SACCH2 =9
STEP_MASHOUT =10
STEP_MASHHOLD =11
STEP_SPARGE =12
STEP_BOIL =13
STEP_CHILL =14
STEP_DONE =15

PROGRAM_IDLE = 255

MASH_DOUGHIN =0
MASH_ACID =1
MASH_PROTEIN =2
MASH_SACCH =3
MASH_SACCH2 =4
MASH_MASHOUT =5

#Zones
ZONE_MASH =0
ZONE_BOIL =1

I2C_ADDR =0x10

stepProgram = [PROGRAM_IDLE] * NUM_BREW_STEPS
preheated = [False] * 4
setpoint = {"MASH_TS_TEMP": 0}
heatstatus = [0,0]
mashVol = 0

temp = [0]*2

BrewConfig = {}

ESTOP = False
