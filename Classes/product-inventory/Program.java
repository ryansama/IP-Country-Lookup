public class Program {
	public static void main(String[] args){
		Inventory inventory = new Inventory();

		inventory.addProduct(new Product(1, "Apple", 2.50, 4));
		inventory.addProduct(new Product(2, "Orange", 1.00, 4));
		inventory.addProduct(new Product(3, "Banana", 0.50, 4));
		inventory.removeProduct(3);
		System.out.println(inventory.toString());
	}
}