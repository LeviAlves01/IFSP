import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
import java.util.Scanner;
import java.nio.file.StandardOpenOption;

public class Main {
    public static void main(String[] args) {

       Path caminho = Path.of("planilha.csv");
       Scanner sc = new Scanner(System.in);

       System.out.print("Digite seu nome e sobrenome: ");
       String nome = sc.nextLine();
       System.out.print("Digite sua idade: ");
       int idade = sc.nextInt();

       String cabecalho = "infos\n";
       String conteudo = nome + "," + idade + "\n";

        try {
            if (!Files.exists(caminho)) {
                Files.createFile(caminho);
                System.out.println("Arquivo criado com sucesso!");

                Files.writeString(caminho, cabecalho, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
                Files.writeString(caminho, conteudo, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
                System.out.println("informação escrita");

            } else {
                System.out.println("O arquivo já existe.");
                Files.writeString(caminho, conteudo, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}