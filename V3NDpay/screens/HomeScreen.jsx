
import React, { useState, useEffect } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Alert, Image } from "react-native";
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import IP_ADDRESS from "../components/IPAddresses";
import NavIcon from "../components/NavIcon";

const HomeScreen = ({ route }) => {
  const navigation = useNavigation();
  const { username } = route.params || { username: "Guest" };
  const [balance, setBalance] = useState(0.0);
  const [dateTime, setDateTime] = useState(new Date());

  useEffect(() => {
    if (username === "Guest") {
      Alert.alert("Guest User", "Please log in to continue.");
      navigation.replace("Login");
    } else {
      fetchBalance();
    }
    const timer = setInterval(() => setDateTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, [username, navigation]);

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

  const loadBalance = async () => {
    try {
      const response = await axios.post(
        `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/load_balance`,
        { username }
      );
      Alert.alert("Success", response.data.message);
      setBalance(response.data.new_balance);
    } catch (error) {
      console.error("Error loading balance:", error.response ? error.response.data : error.message);
      Alert.alert("Error", "Could not load balance.");
    }
  };

  return (
    <View style={styles.container}>
      {/* Header Section */}
      <View style={styles.header}>
      

        <View style={styles.profileSection}>
          
          <Text style={styles.usernameText}>Hi, {username}</Text>
        </View>
        
      </View>
      

      {/* Balance Section */}
      <View style={styles.balanceContainer}>
        <Ionicons name="wallet-outline" size={20} color="#fff" />
        <Text style={styles.balanceLabel}>NPR</Text>
        <Text style={styles.balanceAmount}>{balance.toFixed(2)}</Text>
        <Text style={styles.balanceText}>Balance</Text>
      </View>

      {/* Action Buttons Section */}
      <View style={styles.actionsContainer}>
        <TouchableOpacity style={styles.scanButton} onPress={() => navigation.navigate("ScanToPay", { username })}>
          <Ionicons name="scan" size={28} color="#fff" />
          <Text style={styles.buttonText}>Scan to Pay</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.inventoryButton} onPress={() => navigation.navigate("BrowseInventory", { username })}>
          <Ionicons name="cart" size={28} color="#fff" />
          <Text style={styles.buttonText}>Browse Inventory</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.loadBalanceButton} onPress={loadBalance}>
          <Ionicons name="add" size={28} color="#fff" />
          <Text style={styles.buttonText}>Load Balance</Text>
        </TouchableOpacity>
      </View>

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
    paddingTop: 40,
  },
  header: {
    backgroundColor: "#4CAF50",
    paddingVertical: 10,
    paddingHorizontal: 20,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
  },
  timeText: {
    color: "white",
    fontSize: 16,
  },
  profileSection: {
    flexDirection: "row",
    alignItems: "center",
  },
  profileImage: {
    width: 40,
    height: 40,
    borderRadius: 20,
    marginRight: 10,
  },
  usernameText: {
    color: "white",
    fontSize: 18,
    fontWeight: "bold",
  },
  notificationIcon: {
    marginLeft: 10,
  },
  balanceContainer: {
    backgroundColor: "white",
    margin: 15,
    padding: 20,
    borderRadius: 10,
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 5,
  },
  balanceLabel: {
    fontSize: 18,
    color: "#555",
  },
  balanceAmount: {
    fontSize: 28,
    fontWeight: "bold",
    color: "#2E7D32",
  },
  balanceText: {
    fontSize: 16,
    color: "#777",
  },
  actionsContainer: {
    flexDirection: "row",
    justifyContent: "center", // Centers buttons horizontally
    alignItems: "center",     // Centers buttons vertically
    paddingHorizontal: 20,    // Optional: Add padding to avoid buttons touching the screen edges
    flexWrap: 'wrap',         // Allow buttons to wrap if needed
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
    fontSize: 16,
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
    position: "absolute",
    bottom: 0,
    left: 0,
    right: 0,
  },
});

export default HomeScreen;
