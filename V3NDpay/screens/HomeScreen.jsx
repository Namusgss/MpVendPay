
import React, { useState, useEffect } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Alert } from "react-native";
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import IP_ADDRESS from "../components/IPAddresses";
import NavIcon from "../components/NavIcon";

const HomeScreen = ({ route }) => {
  const navigation = useNavigation();
  const { username } = route.params || { username: "Guest" };
  const [balance, setBalance] = useState(0.0);

  // Redirect guest to login or prompt to log in
  useEffect(() => {
    if (username === "Guest") {
      // Navigate to login screen or display a guest-specific UI
      Alert.alert("Guest User", "Please log in to continue.");
      navigation.replace("Login"); // Replace "Login" with your login screen name
    } else {
      // Fetch balance for logged-in users
      fetchBalance();
    }
  }, [username, navigation]);

  // Fetch user balance from backend
  const fetchBalance = async () => {
    try {
      const response = await axios.get(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_balance`, {
        params: { username },
      });
      setBalance(response.data.balance);
    } catch (error) {
      console.error("Error fetching balance:", error);
      Alert.alert("Error", "Could not fetch balance.");
    }
  };

  // Load balance function
  const loadBalance = async () => {
    try {
      const response = await axios.post(
        `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/load_balance`,
        { username }
      );
      console.log("Response from backend:", response.data); // Log response
      Alert.alert("Success", response.data.message);
      setBalance(response.data.new_balance); // Update balance in the app
    } catch (error) {
      console.error("Error loading balance:", error.response ? error.response.data : error.message);
      Alert.alert("Error", "Could not load balance.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.welcomeText}>Welcome, {username}!</Text>
      <Text style={styles.balanceText}>Your balance is: NPR {balance.toFixed(2)}</Text>

      <TouchableOpacity style={styles.scanButton} onPress={() => navigation.navigate("ScanToPay", { username })}>
        <Ionicons name="scan" size={28} color="#fff" />
        <Text style={styles.buttonText}>Scan to Pay</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.inventoryButton} onPress={() => navigation.navigate("Inventory")}>
        <Ionicons name="cart" size={28} color="#fff" />
        <Text style={styles.buttonText}>Browse Inventory</Text>
      </TouchableOpacity>

      {/* Load Balance Button */}
      <TouchableOpacity style={styles.loadBalanceButton} onPress={loadBalance}>
        <Ionicons name="add" size={28} color="#fff" />
        <Text style={styles.buttonText}>Load Balance</Text>
      </TouchableOpacity>

      {/* Bottom Navigation */}
      <View style={styles.bottomNav}>
        <NavIcon name="Home" icon="home" active onPress={() => {}} />
        <NavIcon name="Statement" icon="document-text" onPress={() => navigation.navigate("Statement", { username })} />
        <NavIcon name="Support" icon="help-circle" onPress={() => navigation.navigate("Support", { username })} />
        <NavIcon name="More" icon="apps" onPress={() => navigation.navigate("More", { username })} />
      </View>
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
    marginBottom: 20,
  },
  loadBalanceButton: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#FF9800",
    padding: 15,
    width: "80%",
    borderRadius: 10,
    marginBottom: 20,
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
    marginLeft: 10,
  },
  bottomNav: {
    flexDirection: "row",
    justifyContent: "space-around",
    paddingVertical: 10,
    backgroundColor: "#fff",
    borderTopWidth: 1,
    borderColor: "#eee",
    position: "absolute", // Pin the bottom navigation to the bottom
    bottom: 0,
    left: 0,
    right: 0,
  },
  navIcon: {
    alignItems: "center",
  },
  navText: {
    fontSize: 12,
    color: "#aaa",
  },
});

export default HomeScreen;
