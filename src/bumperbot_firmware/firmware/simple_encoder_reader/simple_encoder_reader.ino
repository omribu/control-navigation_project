 #define L298N_enA 9
#define L298N_in1 12
#define L298N_in2 13
#define right_encoder_phaseA 3
#define right_encoder_phaseA 5

unsigned int right_encoder_couter = 0;
String right_encoder_sign = "p"
// double right_wheel_mwas_vel = 0.0


void setup() {
  // put your setup code here, to run once:
  pinMode(L298N_enA, OUTPUT);
  pinMode(L298N_in1, OUTPUT);
  pinMode(L298N_in2, OUTPUT);

  digitalWrite(L298N_in1, HIGH);
  digitalWrite(L298N_in2, LOW);

  Serial.begin(115200);
}

void loop() {
  
  analogWrite(L298N_enA, cmd*100);
  
}

Void rightEncoderCallback()
{
  right_encoder_counter++;
  if(digital(right_encoder_phaseB) == High)
  {
    right_encoder_sign = "p";
  }
  else
  {
    right_encoder_sign = "n";
  }
}
