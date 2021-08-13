class Numeros(){
    var numeros: Array[Int] = new Array[Int](100);
    for(i <- 0 until numeros.size){
        numeros(i) = i + 1;
    }

    def extract(n: Int){
        numeros = numeros.filter(_ != n);
    }

    def comprobar(){
        var faltante = 0;
        var bucle = true;
        var i = 0;
        while(i < numeros.size && bucle){
            if(numeros(i) != i + 1){
                faltante = i + 1;
                bucle = false;
            }
            i += 1;
        }
        if (faltante == 0){
            println("No se ha extraido ningun numero")
        }
        else{
            println("El numero extraido es: " + faltante);
        }
    }
}

object main{
    def main(args: Array[String]){
        val numero = new Numeros();
        numero.comprobar();
        print("Que numero quiere extraer: ")
        val n = scala.io.StdIn.readInt();
        if(n > 0 && n <= 100){
            numero.extract(n);
            numero.comprobar();
        }
        else{
            println("El numero debe estar entre 1 y 100");
        }
    }
}