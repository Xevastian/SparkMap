int analog_0 = 0;
int analog_1 = 0;
int analog_2 = 0;
int analog_3 = 0;

int dl = 10;

const int green_LEDs = 3;
const int blue_LEDs = 3;
const int red_LEDs = 3;
const int yellow_LEDs = 3;

int last_analog_0 = 0;
int last_analog_1 = 0;
int last_analog_2 = 0;
int last_analog_3 = 0;

int green_pressed = -1;
int blue_pressed = -1;
int red_pressed = -1;
int yellow_pressed = -1;

int aces;
int cics;
int ceafad;
int cit;
int overall;


void setup()
{
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  Serial.begin(9600);

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

  // Threshold    isOn    Pin
  int keys_green[green_LEDs][3] = {
    {1020, 0, 2},
    {1000, 0, 3},
    {980, 0, 4}
  };

  int keys_blue[blue_LEDs][3] = {
    {1020, 0, 5},
    {1000, 0, 6},
    {980, 0, 7}
  };

  int keys_red[red_LEDs][3] = {
    {1020, 0, 8},
    {1000, 0, 9},
    {980, 0, 10}
  };

  int keys_yellow[yellow_LEDs][3] = {
    {1020, 0, 11},
    {1000, 0, 12},
    {980, 0, 13}
  };


void green_light() {
  analog_0 = analogRead(A0); // Green

  // GREEN LED
  for (int i = 0; i < green_LEDs; ++i) {
    if (analog_0 - last_analog_0 >= keys_green[i][0] - 10) {
      // Update LED state
      if (keys_green[i][1]) {
        keys_green[i][1] = 0;
        //Print number of LEDs on
        aces = 0;
      } else {
        keys_green[i][1] = 1;
        if (keys_green[i][0] >= 1020) {
          aces = 1;
        }
        else if (keys_green[i][0] >= 1000) {
          aces = 2;
        }
        else if (keys_green[i][0] >= 980) {
          aces = 3;
        }
      }
      green_pressed = i;
      break;
    }
  }

  // Update BUTTON state
  last_analog_0 = analog_0;

  // Turn on the LEDs up to and including the pressed button
  for (int i = 0; i <= green_pressed; ++i) {
    if (keys_green[green_pressed][1]) {
      digitalWrite(keys_green[i][2], HIGH);   
    } else {
      digitalWrite(keys_green[i][2], LOW);
      }
    }

    delay(dl);
}

void blue_light() {
  analog_1 = analogRead(A1); // Blue

  // BLUE LED
  for (int i = 0; i < blue_LEDs; ++i) {
    if (analog_1 - last_analog_1 >= keys_blue[i][0] - 10) {
      // Update LED state
      if (keys_blue[i][1]) {
        keys_blue[i][1] = 0;
        //Print number of LEDs on
        cics = 0;
      } else {
        keys_blue[i][1] = 1;
        if (keys_blue[i][0] >= 1020) {
          cics = 1;
        }
        else if (keys_blue[i][0] >= 1000) {
          cics = 2;
        }
        else if (keys_blue[i][0] >= 980) {
          cics = 3;
        }
      }
      blue_pressed = i;
      break;
    }
  }

  // Update BUTTON state
  last_analog_1 = analog_1;

  // Turn on the LEDs up to and including the pressed button
  for (int i = 0; i <= blue_pressed; ++i) {
    if (keys_blue[blue_pressed][1]) {
      digitalWrite(keys_blue[i][2], HIGH);   
    } else {
      digitalWrite(keys_blue[i][2], LOW);
      }
    }

    delay(dl);
}

void yellow_light() {
  analog_2 = analogRead(A2); // Yellow

  // YELLOW LED
  for (int i = 0; i < yellow_LEDs; ++i) {
    if (analog_2 - last_analog_2 >= keys_yellow[i][0] - 10) {
      // Update LED state
      if (keys_yellow[i][1]) {
        keys_yellow[i][1] = 0;
        //Print number of LEDs on
        cit = 0;
      } else {
        keys_yellow[i][1] = 1;
        if (keys_yellow[i][0] >= 1020) {
          cit = 1;
        }
        else if (keys_yellow[i][0] >= 1000) {
          cit = 2;
        }
        else if (keys_yellow[i][0] >= 980) {
          cit = 3;
        }
      }
      yellow_pressed = i;
      break;
    }
  }

  // Update BUTTON state
  last_analog_2 = analog_2;

  // Turn on the LEDs up to and including the pressed button
  for (int i = 0; i <= yellow_pressed; ++i) {
    if (keys_yellow[yellow_pressed][1]) {
      digitalWrite(keys_yellow[i][2], HIGH);   
    } else {
      digitalWrite(keys_yellow[i][2], LOW);
      }
    }

    delay(dl);
}

void red_light() {
  analog_3 = analogRead(A3); // Red

  // RED LED
  for (int i = 0; i < red_LEDs; ++i) {
    if (analog_3 - last_analog_3 >= keys_red[i][0] - 10) {
      // Update LED state
      if (keys_red[i][1]) {
        keys_red[i][1] = 0;
        //Print number of LEDs on
        ceafad = 0;
      } else {
        keys_red[i][1] = 1;
        if (keys_red[i][0] >= 1020) {
          ceafad = 1;
        }
        else if (keys_red[i][0] >= 1000) {
          ceafad = 2;
        }
        else if (keys_red[i][0] >= 980) {
          ceafad = 3;
        }
      }
      red_pressed = i;
      break;
    }
  }

  // Update BUTTON state
  last_analog_3 = analog_3;

  // Turn on the LEDs up to and including the pressed button
  for (int i = 0; i <= red_pressed; ++i) {
    if (keys_red[red_pressed][1]) {
      digitalWrite(keys_red[i][2], HIGH);   
    } else {
      digitalWrite(keys_red[i][2], LOW);
      }
    }

    delay(dl);
}

void loop() {
  green_light();
  blue_light();
  yellow_light();
  red_light();

  overall = aces + cics + ceafad + cit;

  Serial.print("OVERALL: ");
  Serial.print(overall);
  Serial.print(";  [ ACES: ");
  Serial.print(aces);
  Serial.print(", CICS: ");
  Serial.print(cics);
  Serial.print(", CEAFAD: ");
  Serial.print(ceafad);
  Serial.print(", CIT: ");
  Serial.print(cit);
  Serial.println(" ]");

  return;
}