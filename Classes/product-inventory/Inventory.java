import java.util.*;

public class Inventory {
	private Map<Integer, Product> products;

	public Inventory(){
		products = new HashMap<Integer, Product>();
	}

	public float getValue(){
		float value = 0;
		for(int product : products.keySet()){
			value += products.get(product).getPrice();
		}

		return value;
	}

	public void addProduct(Product product){
		products.put(product.getId(), product);
	}

	public Product removeProduct(int id){
		return products.remove(id);
	}

	public String toString(){
		StringBuilder output = new StringBuilder();

		output.append("**********Inventory**********\n");
		for(int product : products.keySet()){
			output.append(products.get(product).toString());
			output.append("\n");
		}
		output.append("*****************************\n");

		return output.toString();
	}
}
