// Define a class named Library
class Library {
    // Attributes of a book
    String title;
    String author;
    int yearPublished;

    // Method to display book details
    void displayBookInfo() {
        System.out.println("Book Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Year Published: " + yearPublished);
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        // Create an object of Library class
        Library book = new Library();
        
        // Set values for the book attributes
        book.title = "To Kill a Mockingbird";
        book.author = "Harper Lee";
        book.yearPublished = 1960;

        // Call method to display book information
        book.displayBookInfo();
    }
}