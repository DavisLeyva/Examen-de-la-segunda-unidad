// la variable pulso contiene los datos brutos entrantes pudiendo variar entre 0-1024
float pulso;
int alto;
int BPM;
float sensor;
float temp;


// Determina qué señal “se contará como un latido” y qué señal ignorar.
int limite = 522;//original 550- Ver los picos en Ploter y reprogramar

void setup() {
Serial.begin(9600);
}
void loop() {

pulso = analogRead(A0);
sensor = analogRead(A1);

BPM = (60/(float(pulso)/1000));

temp =((sensor*5000.0)/1023)/10;

Serial.print(BPM);
Serial.print("/");
Serial.println(temp);

if(pulso > limite){
//Serial.println(alto);
}

delay(500);
}
