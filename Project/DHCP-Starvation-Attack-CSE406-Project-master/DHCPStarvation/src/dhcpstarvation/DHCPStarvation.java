/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dhcpstarvation;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

class ReadingFileWhileWrite extends Thread {

    boolean running = true;

    //  BufferedInputStream reader = null;
    BufferedReader reader;

    public void run() {
        try {
            sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(ReadingFileWhileWrite.class.getName()).log(Level.SEVERE, null, ex);
        }
        while (running) {
            
            try {
                String line = reader.readLine();

                if (line == null) {
                    System.out.print("");
                } else {

                    System.out.println(line);

                    if (line.startsWith("@")) {
                        line = line.substring(1);
                    }
                    String[] arr = line.split("#");
                    if (arr.length == 11) {
                        for (String a : arr) {
                            System.out.println(a);
                        }
                        String newL = line;
                        Platform.runLater(new Runnable() {
                            @Override
                            public void run() {
                                DHCPStarvation.textArea.appendText(newL);
                                DHCPStarvation.textArea.appendText("\n");
                                DHCPStarvation.table.getItems().add(new DHCP_Packet(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5].substring(0, arr[5].length()-1), arr[6], arr[7], arr[8], arr[9], arr[10]));
                            }
                        });
                    }
                }

            } catch (IOException e) {

                e.printStackTrace();

            }

        }

    }

}

/**
 *
 * @author gahab
 */
public class DHCPStarvation extends Application {

    static TextArea textArea = new TextArea();
    static TableView<DHCP_Packet> table = new TableView<DHCP_Packet>();
     static Process p;

    @Override
    public void start(Stage primaryStage) throws FileNotFoundException {
        table.setEditable(true);

        TableColumn col1 = new TableColumn("Packet Type");
        col1.setMinWidth(100);
        col1.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("type"));
        table.getColumns().add(col1);

        TableColumn col2 = new TableColumn("Source Port");
        col2.setMinWidth(50);
        col2.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("srcPort"));
      //  table.getColumns().add(col2);

        TableColumn col3 = new TableColumn("Destination Port");
        col3.setMinWidth(50);
        col3.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("destPort"));
      //  table.getColumns().add(col3);

        TableColumn col4 = new TableColumn("Source IP");
        col4.setMinWidth(150);
        col4.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("srcIP"));
        table.getColumns().add(col4);

        TableColumn col5 = new TableColumn("Destination IP");
        col5.setMinWidth(200);
        col5.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("destIP"));
        table.getColumns().add(col5);

        TableColumn col6 = new TableColumn("Client Hardware Address");
        col6.setMinWidth(200);
        col6.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("chaddr"));
        table.getColumns().add(col6);

        TableColumn col7 = new TableColumn("Client IP");
        col7.setMinWidth(150);
        col7.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("ciaddr"));
      //  table.getColumns().add(col7);

        TableColumn col8 = new TableColumn("Offered IP");
        col8.setMinWidth(150);
        col8.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("yiaddr"));
        table.getColumns().add(col8);

        TableColumn col9 = new TableColumn("Server IP");
        col9.setMinWidth(150);
        col9.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("siaddr"));
      //  table.getColumns().add(col9);

        TableColumn col10 = new TableColumn("Gateway IP");
        col10.setMinWidth(150);
        col10.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("giaddr"));
       // table.getColumns().add(col10);

        TableColumn col11 = new TableColumn("Transaction ID");
        col11.setMinWidth(150);
        col11.setCellValueFactory(
                new PropertyValueFactory<DHCP_Packet, String>("xid"));
        table.getColumns().add(col11);
        Button btn = new Button();
        ReadingFileWhileWrite tw = new ReadingFileWhileWrite();
        textArea.setEditable(false);

        btn.setText("Start DHCP Starvation Attack");

        Button btn2 = new Button();

        btn2.setText("Stop DHCP Starvation Attack");
        btn2.setDisable(true);
        Label l1 = new Label("Interface:    ");
        TextField tf1 = new TextField();
        Label warning = new Label("You must enter an interface");
        warning.setVisible(false);
        textArea.appendText("OFFERED IP ADDRESSES BY THE DHCP SERVER"
                + "\n");
       
        btn.setOnAction(new EventHandler<ActionEvent>() {

            @Override
            public void handle(ActionEvent event) {
                try {

                    String interfaceName = tf1.getText();
                    if (interfaceName.equals("") == true) {

                        warning.setVisible(true);
                    } else {
                        btn.setDisable(true);
                        btn2.setDisable(false);
                        System.out.println("Hello World!");

                        try {
                            System.out.println("Running shell script");

                            String[] cmd = {"sh", "/home/gahab/NetBeansProjects/DHCPStarvation/script.sh", interfaceName};
                            p = Runtime.getRuntime().exec(cmd);
                            File file = new File("new.txt");

                            tw.reader = new BufferedReader(new FileReader(file));

                            tw.start();

                        } catch (Exception ex) {
                            Logger.getLogger(DHCPStarvation.class.getName()).log(Level.SEVERE, null, ex);
                        }

                        //You can use these methods
                        textArea.setPrefHeight(500);  //sets height of the TextArea to 400 pixels 
                        textArea.setPrefWidth(500);

                        //   VBox vbox = new VBox(textArea);
                        final VBox vbox = new VBox();
                        vbox.setSpacing(5);
                        vbox.setMaxSize(800, 800);
                        vbox.setPadding(new Insets(5, 0, 0, 5));
                        vbox.getChildren().addAll(table);
                        Scene secondScene = new Scene(vbox, 500, 500);
                        secondScene.getStylesheets().add("startPageDesign.css");
                        // New window (Stage)
                        Stage newWindow = new Stage();
                        newWindow.setTitle("Packet details");
                        newWindow.setScene(secondScene);

                        // Set position of second window, related to primary window.
                        newWindow.setX(primaryStage.getX() + 200);
                        newWindow.setY(primaryStage.getY() + 100);

                        newWindow.show();
                    }

                } catch (Exception ex) {
                    Logger.getLogger(DHCPStarvation.class.getName()).log(Level.SEVERE, null, ex);
                }

            }
        });

        btn2.setOnAction(new EventHandler<ActionEvent>() {

            @Override
            public void handle(ActionEvent event) {
                
                tw.running = false;
                try {
                    tw.reader.close();
                } catch (IOException ex) {
                    Logger.getLogger(DHCPStarvation.class.getName()).log(Level.SEVERE, null, ex);
                }
                btn.setDisable(true);
                btn2.setDisable(true);
                p.destroyForcibly();
                
                 String[] cmd = {"sh", "/home/gahab/NetBeansProjects/DHCPStarvation/killer.sh"};
                try {
                    Process  killP = Runtime.getRuntime().exec(cmd);
                    killP.waitFor();
                } catch (Exception ex) {
                    Logger.getLogger(DHCPStarvation.class.getName()).log(Level.SEVERE, null, ex);
                }

            }
        });

        GridPane root = new GridPane();
        root.setAlignment(Pos.CENTER);
        root.setHgap(10);
        root.setVgap(10);
        root.add(l1, 0, 0);
        root.add(tf1, 1, 0);

        root.add(btn, 1, 1);
        root.add(btn2, 1, 2);

        root.add(warning, 1, 3);
        Scene scene = new Scene(root, 600, 600);
        scene.getStylesheets().add("startPageDesign.css");
        primaryStage.setTitle("DHCP STARVATION !!!!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException {

        launch(args);
    }

}
