#include <iostream>
#include<map>
#include<utility>
#include <string>
using namespace std;

class Animal{
  private:
    string nombre;
    string codigo;
  public:
  Animal(string n,string c){
    nombre=n;
    codigo=c;
  }
  Animal(){
  }
  string getNombre(){
    return nombre;
  }
  string getCodigo(){
    return codigo;
  }
};

class Zoo{
  private:
    string nombre;
    map <string,Animal> directorio;
  public:
    Zoo(){
    }
    void agregarAnimal(Animal a){
      directorio[a.getCodigo()]=a;
    }
    void consultarAnimal(string c){
      cout << "Consultando por el código de jaula " << c << " ..." << endl;
      if(directorio.find(c)!=directorio.end()){
        cout << "El animal que está dentro de la jaula " << c << " es un " << directorio[c].getNombre() << "." << endl;
      }
      else{
        cout << "La jaula " << c << " no existe." << endl;
      }
    }
    void imprimirDirectorio(){
      cout << "Actualmente hay " << directorio.size() << " animales registrados. Estos son: " << endl;
      for(map <string,Animal>::iterator i=directorio.begin();i!=directorio.end();i++){
        cout << (i->second).getNombre() << endl;
      }
    }
};

int main() {
  Zoo z;
  Animal e("Elefante","1");
  Animal f("Foca","2");
  Animal l("León","231415");
  Animal zo("Zorro","49");
  Animal m("Mono","311");
  z.agregarAnimal(e);
  z.agregarAnimal(f);
  z.agregarAnimal(l);
  z.agregarAnimal(zo);
  z.agregarAnimal(m);
  z.imprimirDirectorio();
  z.consultarAnimal("59");
  z.consultarAnimal("311");
}