  int segments[7] = {5, 6, 7, 8, 9, 10, 11};
  int push_button = 12;
  int buzzer = 13;
  int target;
  int gameSpeed = 1000;
  const byte digitMap[10][7] ={
    // fill the byte values of each segment for each digit one by one
    //0
    //1
    //3
    //4
    //5
    //6
    //7
    //8
    //9
  }
void setup() {
  for int(i=0; i<7; i++){
    pinMode(segments[i], OUTPUT);
  }
  pinMode(push_botton, INPUT_PULLUP); // For connecting the push_button to 5V arduino supply so that it stays HIGH when not pressed
  pinMode(buzzer, OUTPUT);
  randomseed(analogread(19)); //Ensure A0 is not connected to anything 
  target = random(0, 10);
  }
}

void displayDigit(int num){
  for (int i=0; i<7; i++){
    digitalWrite(segments[i], digitMap[num][i]);
  }

void victory(){
  for (int j=0; j<3; j++){
    tone(buzzer, 2000, 100); 
    delay(100);
  }
}
void defeat(){
  tone(buzzer, 200, 1000);
  delay(1000);
}

void loop() {
  for int(i=0; i<=9; i++){
    s=displayDigit[i];
    tone(buzzer, 1000, 20) //(pin, sound frequency, duration of sound (ms))
 
    unsigned long startTime = millis(); //counts how much time has passed

    while(millis()-startTime<gameSpeed){
      if (digitalRead(push_button)==LOW){
        if (i==target){
          victory();
        }
        else{
          defeat();
        }
        target = random(0, 10);
        return // restarts the game
      }
  }
  }


}
