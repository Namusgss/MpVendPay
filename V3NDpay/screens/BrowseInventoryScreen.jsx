import React, { useState, useEffect } from "react";
import { View, Text, FlatList, Image, StyleSheet, TouchableOpacity, ActivityIndicator, Alert } from "react-native";
import axios from "axios";
import IP_ADDRESS from "../components/IPAddresses"; // Replace with your IP address configuration

const BrowseInventoryScreen = () => {
  const [inventory, setInventory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch inventory data when the component mounts
    const fetchInventory = async () => {
      try {
        const response = await axios.get(
          `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_inventory`
        );
        setInventory(response.data);
      } catch (error) {
        Alert.alert("Error", "Failed to load inventory.");
      } finally {
        setLoading(false);
      }
    };

    fetchInventory();
  }, []);

  const renderItem = ({ item }) => (
    <View style={styles.productCard}>
      <Image source={{ uri: item.imageUrl }} style={styles.productImage} />
      <View style={styles.productInfo}>
        <Text style={styles.productName}>{item.productName}</Text>
        <Text style={styles.productQuantity}>Available Quantity: {item.quantity}</Text>
        <Text style={styles.productPrice}>Price: NPR {item.price}</Text>
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      {loading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <FlatList
          data={inventory}
          renderItem={renderItem}
          keyExtractor={(item) => item.productName}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    padding: 10,
  },
  productCard: {
    flexDirection: "row",
    marginBottom: 15,
    padding: 10,
    backgroundColor: "#f9f9f9",
    borderRadius: 10,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 3,
  },
  productImage: {
    width: 60,
    height: 60,
    borderRadius: 10,
    marginRight: 15,
  },
  productInfo: {
    justifyContent: "center",
  },
  productName: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#333",
  },
  productQuantity: {
    fontSize: 16,
    color: "#555",
  },
  productPrice: {
    fontSize: 16,
    color: "#4CAF50",
  },
  viewButton: {
    backgroundColor: "#4CAF50",
    padding: 10,
    borderRadius: 5,
    marginTop: 10,
  },
  viewButtonText: {
    color: "#fff",
    fontWeight: "bold",
  },
});

export default BrowseInventoryScreen;
