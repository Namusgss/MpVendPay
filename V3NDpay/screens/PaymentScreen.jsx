
// import React from "react";
// import { View, Text, TouchableOpacity, StyleSheet, Alert } from "react-native";
// import { useRoute, useNavigation } from "@react-navigation/native";
// import axios from "axios";
// import IP_ADDRESS from "../components/IPAddresses";  

// const PaymentScreen = () => {
//   const route = useRoute();
//   const navigation = useNavigation();
//   const { username, productName, quantity, amount } = route.params || {
//     username: "Guest",
//     productName: "Unknown",
//     quantity: 1,
//     amount: 0.0,
//   };

//   // Handle Payment & Deduct from Database
//   const handlePayment = async () => {
//     console.log("🔄 Processing payment...");
//     console.log("Username:", username);  // Debugging line
//     console.log("Amount:", amount);  // Debugging line

//     // Validate amount
//     if (isNaN(amount) || amount <= 0) {
//       Alert.alert("Error", "Invalid amount");
//       return;
//     }

//     // Alert.alert("Processing Payment", `You are paying NPR ${amount} for ${quantity}x ${productName}.`);

//     try {
//       // ✅ Process Payment (Deduct from Database)
//       const paymentResponse = await axios.post(
//         `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/process_payment`,
//         {
//           username: username,  // ✅ Ensure correct username format
//           amount: parseFloat(amount),  // ✅ Ensure amount is a float
//         },
//         {
//           headers: { "Content-Type": "application/json" },
//         }
//       );

//       console.log("✅ Payment Success:", paymentResponse.data);
    
//        // After successful payment, save the transaction
//        const purchaseRecord = {
//         username,
//         productName,
//         quantity,
//         amount: parseFloat(amount),
//     };

//     const saveTransactionResponse = await axios.post(
//         `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/save_transaction`,
//         purchaseRecord,
//         {
//             headers: { "Content-Type": "application/json" },
//         }
//     );

//     console.log("✅ Transaction saved:", saveTransactionResponse.data);

//       // ✅ Show success alert
//       Alert.alert("Payment Successful", `You have paid NPR ${amount} for ${quantity}x ${productName}.`);

//       // ✅ Navigate back to HomeScreen with username
//       navigation.replace("Home", { username });

//     } catch (error) {
//       console.error("❌ Payment error:", error);

//       let errorMessage = "Transaction failed.";
//       if (error.response) {
//         errorMessage = error.response.data?.detail || error.response.data?.message || errorMessage;
//       }

//       Alert.alert("Error", errorMessage);
//     }
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.header}>Confirm Your Payment</Text>

//       <View style={styles.paymentCard}>
//         <Text style={styles.productName}>{productName}</Text>
//         <Text style={styles.details}>Quantity: {quantity}</Text>
//         <Text style={styles.amount}>Total: NPR {parseFloat(amount).toFixed(2)}/-</Text>
//       </View>

//       <TouchableOpacity style={styles.payButton} onPress={handlePayment}>
//         <Text style={styles.buttonText}>Pay Now</Text>
//       </TouchableOpacity>

//       <TouchableOpacity style={styles.cancelButton} onPress={() => navigation.goBack()}>
//         <Text style={styles.cancelText}>Cancel</Text>
//       </TouchableOpacity>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#E8F5E9",
//     justifyContent: "center",
//     alignItems: "center",
//     padding: 20,
//   },
//   header: {
//     fontSize: 24,
//     fontWeight: "bold",
//     color: "#2E7D32",
//     marginBottom: 20,
//   },
//   paymentCard: {
//     backgroundColor: "#fff",
//     width: "90%",
//     padding: 20,
//     borderRadius: 10,
//     alignItems: "center",
//     shadowColor: "#000",
//     shadowOpacity: 0.1,
//     shadowRadius: 5,
//     elevation: 5,
//   },
//   productName: {
//     fontSize: 22,
//     fontWeight: "bold",
//     marginVertical: 10,
//     color: "#333",
//   },
//   details: {
//     fontSize: 18,
//     color: "#666",
//   },
//   amount: {
//     fontSize: 24,
//     fontWeight: "bold",
//     color: "#388E3C",
//     marginTop: 10,
//   },
//   payButton: {
//     backgroundColor: "#4CAF50",
//     padding: 15,
//     borderRadius: 10,
//     marginTop: 20,
//     width: "80%",
//     alignItems: "center",
//   },
//   buttonText: {
//     color: "#fff",
//     fontSize: 18,
//     fontWeight: "bold",
//   },
//   cancelButton: {
//     marginTop: 15,
//   },
//   cancelText: {
//     fontSize: 16,
//     color: "#D32F2F",
//   },
// });

// export default PaymentScreen;


import React from "react";
import { View, Text, TouchableOpacity, StyleSheet, Alert } from "react-native";
import { useRoute, useNavigation } from "@react-navigation/native";
import axios from "axios";
import IP_ADDRESS from "../components/IPAddresses";

const PaymentScreen = () => {
  const route = useRoute();
  const navigation = useNavigation();
  const { username, productName, quantity, amount } = route.params || {
    username: "Guest",
    productName: "Unknown",
    quantity: 1,
    amount: 0.0,
  };

  // Handle Payment & Save Transaction with Date/Time
  const handlePayment = async () => {
    console.log("🔄 Processing payment...");
    console.log("Username:", username);
    console.log("Amount:", amount);

    // Validate amount
    if (isNaN(amount) || amount <= 0) {
      Alert.alert("Error", "Invalid amount");
      return;
    }

    try {
      // Get current date & time
      const transactionTime = new Date().toISOString(); // Saves in ISO format (YYYY-MM-DDTHH:mm:ss.sssZ)

      // ✅ Process Payment (Deduct from Database)
      const paymentResponse = await axios.post(
        `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/process_payment`,
        {
          username: username,
          amount: parseFloat(amount),
        },
        { headers: { "Content-Type": "application/json" } }
      );

      console.log("✅ Payment Success:", paymentResponse.data);

      // ✅ Save Transaction with Date/Time
      const purchaseRecord = {
        username,
        productName,
        quantity,
        amount: parseFloat(amount),
        transactionDate: new Date().toISOString().split("T")[0], // Extract date (YYYY-MM-DD)
        transactionTime: new Date().toLocaleTimeString(), // Extract time (HH:MM:SS)
      };

      const saveTransactionResponse = await axios.post(
        `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/save_transaction`,
        purchaseRecord,
        { headers: { "Content-Type": "application/json" } }
      );

      console.log("✅ Transaction saved:", saveTransactionResponse.data);

      // ✅ Show success alert
      Alert.alert(
        "Payment Successful",
        `You paid NPR ${amount} for ${quantity}x ${productName} on ${new Date(transactionTime).toLocaleString()}.`
      );

      // ✅ Navigate back to HomeScreen with username
      navigation.replace("Home", { username });

    } catch (error) {
      console.error("❌ Payment error:", error);
      
      let errorMessage = "Transaction failed. Please try again.";
      if (error.response) {
        errorMessage = error.response.data?.detail || error.response.data?.message || errorMessage;
      }

      Alert.alert("Error", errorMessage);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Confirm Your Payment</Text>

      <View style={styles.paymentCard}>
        <Text style={styles.productName}>{productName}</Text>
        <Text style={styles.details}>Quantity: {quantity}</Text>
        <Text style={styles.amount}>Total: NPR {parseFloat(amount).toFixed(2)}/-</Text>
      </View>

      <TouchableOpacity style={styles.payButton} onPress={handlePayment}>
        <Text style={styles.buttonText}>Pay Now</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.cancelButton} onPress={() => navigation.goBack()}>
        <Text style={styles.cancelText}>Cancel</Text>
      </TouchableOpacity>
    </View>
  );
};

// 🎨 Styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#E8F5E9",
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  header: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 20,
  },
  paymentCard: {
    backgroundColor: "#fff",
    width: "90%",
    padding: 20,
    borderRadius: 10,
    alignItems: "center",
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 5,
  },
  productName: {
    fontSize: 22,
    fontWeight: "bold",
    marginVertical: 10,
    color: "#333",
  },
  details: {
    fontSize: 18,
    color: "#666",
  },
  amount: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#388E3C",
    marginTop: 10,
  },
  payButton: {
    backgroundColor: "#4CAF50",
    padding: 15,
    borderRadius: 10,
    marginTop: 20,
    width: "80%",
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
  },
  cancelButton: {
    marginTop: 15,
  },
  cancelText: {
    fontSize: 16,
    color: "#D32F2F",
  },
});

export default PaymentScreen;
