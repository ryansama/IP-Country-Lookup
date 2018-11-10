public class Product {
	private int id;
	private String name;
	private double price;
	private int quantity;

	public Product(int id, String name, double price, int quantity){
		this.id = id;
		this.name = name;
		this.price = price;
		this.quantity = quantity;
	}

	public int getId(){
		return this.id;
	}

	public void setId(int id){
		this.id = id;
	}

	public String getName(){
		return this.name;
	}

	public void setName(String name){
		this.name = name;
	}

	public double getPrice(){
		return this.price;
	}

	public void setPrice(double price){
		this.price = price;
	}

	public int getQuantity(){
		return this.id;
	}

	public void setQuantity(int quantity){
		this.quantity = quantity;
	} 

	public String toString(){
		return String.format("Id: %d, Name: %s, Price: %f, Quantity: %d", 
								this.id, this.name, this.price, this.quantity);  
	}
}