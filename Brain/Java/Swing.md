# 기본 탬플릿
```java
class MyFrame extends JFrame {
	private static final long serialVersionUID = 1L;

	void createAndShowGUI() {
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		addCompoenetsToPane();
		setPreferredSize(new Dimension(300, 300));
		pack();
		setVisible(true);
	}

	void addCompoenetsToPane() {

	}
}

public class Pr02 {
	public static void main(String[] args) {
		MyFrame frame = new MyFrame();
		frame.createAndShowGUI();
	}
}
```


# 램덤색
RGB 각각 0~255
```java
Color randColor = new Color((int) (Math.random() * 256), (int) (Math.random() * 256), (int) (Math.random() * 256))
```


# 원 그리기

```java
class CirclePanel extends JPanel{
	private static final long serialVersionUID = 1L;

	public CirclePanel() {
		this.setPreferredSize(new Dimension(50, 50)); // 원하는 크기를 설정
		this.setOpaque(false); // 패널 배경을 투명하게 설정
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		g.drawOval(10, 10, 50, 50); // x, y, width, height
	}
}
```

```java
//램덤한 위치에 원 그리기
int rndx = (int) (Math.random() * 500);
int rndy = (int) (Math.random() * 500);
g.drawOval(rndx, rndy, 50, 50);
g.fillOval(rndx, rndy, 50, 50);
```