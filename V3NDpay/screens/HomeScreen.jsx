import React, { useState, useEffect } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Alert } from "react-native";
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import IP_ADDRESS from "../components/IPAddresses";

const HomeScreen = ({ route }) => {
  const navigation = useNavigation();
  const { username } = route.params || { username: "Guest" };
  const [balance, setBalance] = useState(0.0);

  // ✅ Fetch user balance from backend
  useEffect(() => {
    const fetchBalance = async () => {
      try {
        const response = await axios.get(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_balance`, {
          params: { username },
        });
        setBalance(response.data.balance);
      } catch (error) {
        console.error("❌ Error fetching balance:", error);
        Alert.alert("Error", "Could not fetch balance.");
      }
    };

    fetchBalance();
  }, [username]); // ✅ Runs when `username` changes

  return (
    <View style={styles.container}>
      <Text style={styles.welcomeText}>Welcome, {username}!</Text>
      <Text style={styles.balanceText}>Your balance is: ${balance.toFixed(2)}</Text>

      <TouchableOpacity style={styles.scanButton} onPress={() => navigation.navigate("ScanToPay", { username })}>
        <Ionicons name="scan" size={28} color="#fff" />
        <Text style={styles.buttonText}>Scan to Pay</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.inventoryButton} onPress={() => navigation.navigate("Inventory")}>
        <Ionicons name="cart" size={28} color="#fff" />
        <Text style={styles.buttonText}>Browse Inventory</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#E8F5E9",
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 10,
  },
  balanceText: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#388E3C",
    marginBottom: 30,
  },
  scanButton: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#4CAF50",
    padding: 15,
    width: "80%",
    borderRadius: 10,
    marginBottom: 20,
  },
  inventoryButton: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#2E7D32",
    padding: 15,
    width: "80%",
    borderRadius: 10,
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
    marginLeft: 10,
  },
});

export default HomeScreen;
