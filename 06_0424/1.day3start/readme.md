우선 해야 하는 것이 
GPIO 핀이 OUTPUT/INPUT 모드인지 세팅
해당 핀에 입력장치 또는 출력장치를 연결하고
이후 개발자가 직접 ㅆ는 것

필요 명령어
sudo mknod /dev/nobrand c 100 0
sudo chmod 666 /dev/nobrand
source alias.sh
