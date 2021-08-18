using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Välkommen till denna Pensionsimulator");
    Console.WriteLine ("-------------------------------------");
    Console.WriteLine ("Vad heter du i förnamn?");
    string name = Console.ReadLine();
    Console.WriteLine ("Hur gammal är du?");
    int age = Convert.ToInt16(Console.ReadLine());
    Console.WriteLine ("I vilken ålder vill gå i pension?");
    int pension = Convert.ToInt16(Console.ReadLine());
    years_to_pension = pension - age;
    Console.WriteLine ("Hej " + name + ". Du vill gå i pension när du är " + pension + " år vilket är om " + years_to_pension + " år.");
    }
  } 
}

