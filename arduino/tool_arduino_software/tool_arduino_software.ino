void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Set pins 0 to 3 of PORTB as outputs
  DDRB = 0b00001111;

  // PORTD as input
  // Enable PORTD internal pull up resitors
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);

}

int command, data, port_val;


void loop() {
  // Set a value for pins 0 to 3 of PORTB
  
  // If a value is received set it to the output port
  if (Serial.available() > 0)
  {

    command = Serial.parseInt();
    // 1 set port value
    if(command == 1)
    {
      while(1)
      {
        if (Serial.available() > 0)
        {
          break;
        }
      }
      delay(50);
      data = Serial.parseInt();
      set_gpio_value(data);

    }
    // 2 get port value
    else if(command == 2)
    {
      port_val = get_gpio_value();
      Serial.println(port_val);
    }
  
  }


}

/*******************************************************/
void set_gpio_value(int value)
{
  // Set port
  PORTB = value;
}

int get_gpio_value(void)
{

  int port_value;

  port_value = (PIND & 240) >> 4;

  return port_value;

}


