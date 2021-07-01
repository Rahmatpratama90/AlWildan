import java.util.*;

class Checker implements Comparator<Player> { //bikin class untuk Chekcer implements Comparator<Player>


  public int compare(Player a,  Player b) {
      if (a.score > b.score) { //bikin kondisi yagn diminta , dimulai dari jika score a lebih besar dari score b 
        return -1; //return nilai -1
    } else if (a.score < b.score) { //jika score a lebih besar dari score b
        return 1; //return nilai 1
    } else { //jika tidak keduanya
        return a.name.compareTo(b.name); //return nilai name a dicompare dengan name b
    }
  }
}



class Player { //bikin class Player
  String name; //bikin variabel name tipe data string
  int score; //bikin variabel score tipe data integer

  Player(String name, int score){ 
    this.name = name; 
    this.score = score; 
  }
}

public class Solution {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in); //scan sebagai Scanner dibuat sama dengan new scanner(Systems.in)
    int n = scan.nextInt(); //int n seagai scan.nexInt

    Player[] player = new  Player[n]; 
    Checker checker = new Checker(); 

    for(int i = 0; i < n; i++){ //for loop ketika i sama dengan 0 i kurang dari n maka i akan bertambah2
      Player[i] = new  Player(scan.next(), scan.nextInt());
    }
    scan.close(); //close scan 

    Arrays.sort(player, checker); //sort daripada variabel player dan checker
    for(int i = 0; i < player.length; i++){ //ketika i = 0  kurang dari player.length , maka i akan bertambah2
      System.out.printf("%s %s\n", player[i].name, player[i].score); //print
    }
  }
}