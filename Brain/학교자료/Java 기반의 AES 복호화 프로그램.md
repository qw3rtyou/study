# 코드
```java
import java.util.Base64;  
import javax.crypto.Cipher;  
import javax.crypto.spec.IvParameterSpec;  
import javax.crypto.spec.SecretKeySpec;  
  
public class AESDecryption {  
    public static void main(String[] args) {  
        try {  
            String key = "8iE3bf1se6N76HGPP8S0Xw==";  
            String iv = "cHml3oX848/0uBwDJtChOA==";  
            String ciphertext = "QDr9NZNG9Bgc3TTnfRuqjjzf/kVSYwbP7F9mR4GQZ/IneIh7HTc/xnwzEeVBcH3pPlIbLFySKZruedJc9X87CGNDJ1f2Dat8BR3Ypbei5Q42xc306/AkSuGsjfqbX9/ELxmdKn7MyvY/Jbc0v0AJHV6odgNzygKRRrFJcUIF/50=";  
            //먼저 인코딩 데이터를 디코딩 해줌  
            byte[] decodedKey = Base64.getDecoder().decode(key);  
            byte[] decodedIV = Base64.getDecoder().decode(iv);  
            byte[] decodedCiphertext = Base64.getDecoder().decode(ciphertext);  
            //출력함  
            System.out.println(decodedKey);  
            System.out.println(decodedIV);  
            System.out.println(decodedCiphertext);  
  
            //키와 이니셜벡터 담는 클래스 초기화  
            SecretKeySpec secretKeySpec = new SecretKeySpec(decodedKey, "AES");  
            IvParameterSpec ivParameterSpec = new IvParameterSpec(decodedIV);  
  
            //복호화할 암호문 설정값을 문제에 나와있는대로 세팅  
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");  
            cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, ivParameterSpec);  
  
            //복호화  
            byte[] decryptedBytes = cipher.doFinal(decodedCiphertext);  
            String plaintext = new String(decryptedBytes);  
  
            System.out.println("복호화 결과: " + plaintext);  
            //try-catch문 없으면 오류남  
        } catch (Exception e) {  
            e.printStackTrace();  
        }  
    }  
}
```


# 실행결과
```
"C:\Program Files\Java\jdk-20\bin\java.exe" "-javaagent:D:\JetBrains\IntelliJ IDEA 2023.3.2\lib\idea_rt.jar=57695:D:\JetBrains\IntelliJ IDEA 2023.3.2\bin" -Dfile.encoding=UTF-8 -Dsun.stdout.encoding=UTF-8 -Dsun.stderr.encoding=UTF-8 -classpath [실행디렉토리] AESDecryption
[B@2f4d3709
[B@4e50df2e
[B@1d81eb93
복호화 결과: Hello world of AES encryption. A secret between two is a secret of God; a secret among three is everybody's secret.

Process finished with exit code 0

```

# 복호화된 plaintext
```
Hello world of AES encryption. A secret between two is a secret of God; a secret among three is everybody's secret.
```
