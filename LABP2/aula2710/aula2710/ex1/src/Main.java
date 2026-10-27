import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
import java.nio.file.StandardOpenOption;

public class Main {
    public static void main(String[] args) throws IOException {
        Path caminho = Path.of("myway.txt");
        String conteudo = "13 é Lula\n";

        try {
            if (!Files.exists(caminho)) {
                Files.createFile(caminho);
                System.out.println("Arquivo criado com sucesso!");
            } else {
                System.out.println("O arquivo já existe.");
            }

            for(int i = 1; i<=3765; i++){
                Files.writeString(
                    caminho,
                    conteudo,
                            StandardOpenOption.CREATE, StandardOpenOption.APPEND
                );
            };
        } catch (IOException e) {
            e.printStackTrace();
        }




    }
}