import java.util.*;

class Checker implements Comparator<Pemain> { //bikin class untuk Chekcer implements Comparator<Pemain>

  @Override
  public int compare(Pemain a,  Pemain b) {
      if (a.skor > b.skor) { //bikin kondisi yagn diminta , dimulai dari jika skor a lebih besar dari skor b 
        return -1; //return nilai -1
    } else if (a.skor < b.skor) { //jika skor a lebih besar dair skor b
        return 1; //return nilai 1
    } else { //jika tidak keduanya
        return a.nama.compareTo(b.nama); //return nilai nama a dicompare dengan nama b
    }
  }
}

class Pemain { //bikin class Pemain
  String nama; //bikin variabel nama tipe data string
  int skor; //bikin variabel score tipe data integer

  Pemain(String nama, int skor){ 
    this.nama = nama; 
    this.skor = skor; 
  }
}

public class Solution {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in); //scan sebagai Scanner dibuat sama dengan new scanner(Systems.in)
    int n = scan.nextInt(); //int n seagai scan.nexInt

    Pemain[] pemain = new  Pemain[n]; 
    Checker checker = new Checker(); 

    for(int i = 0; i < n; i++){ //for loop ketika i sama dengan 0 i kurang dari n maka i akan bertambah2
      Pemain[i] = new  Pemain(scan.next(), scan.nextInt());
    }
    scan.close(); //close scan 

    Arrays.sort(pemain, checker); //sort daripada variabel pemain dan checker
    for(int i = 0; i < pemain.length; i++){ //ketika i = 0  kurang dari pemain.length , maka i akan bertambah2
      System.out.printf("%s %s\n", pemain[i].name, pemain[i].score); //print
    }
  }
}