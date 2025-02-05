
import React, { useEffect, useState } from "react";
import { View, Text, FlatList, StyleSheet, ActivityIndicator, Alert } from "react-native";
import { useRoute, useNavigation} from "@react-navigation/native";
import IP_ADDRESS from "../components/IPAddresses";
import NavIcon from "../components/NavIcon";

const StatementScreen = () => {
  const route = useRoute();
  const navigation = useNavigation();  
  const username = route.params?.username || "Guest"; // Fallback if username is not available
  console.log("Username in StatementScreen:", username);

  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Ensure username is available before fetching data
    if (username && username !== "Guest") {
      console.log("Fetching purchase history for:", username);
      fetch(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_purchase_history?username=${username}`)
        .then((response) => response.json())
        .then((data) => {
          // Check for empty response
          setHistory(data.message ? [] : data);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error fetching history:", error);
          setLoading(false);
          Alert.alert("Error", "Failed to fetch purchase history. Please try again.");
        });
    } else {
      setLoading(false);
    }
  }, [username]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Purchase History for {username}</Text>
      {loading ? (
        <ActivityIndicator size="large" color="#2E7D32" />
      ) : history.length === 0 ? (
        <Text style={styles.noData}>No transactions found.</Text>
      ) : (
        <FlatList
          data={history}
          keyExtractor={(item, index) => index.toString()}
          renderItem={({ item }) => (
            <View style={styles.card}>
              <Text style={styles.productName}>{item.productName}</Text>
              <Text>Quantity: {item.quantity}</Text>
              <Text>Amount: NPR {item.amount}</Text>
            </View>
          )}
        />
      )}
      <View style={styles.bottomNav}>
        <NavIcon name="Home" icon="home" onPress={() => navigation.navigate("Home", { username })} />
        <NavIcon name="Statement" icon="document-text" active onPress={() => {}} />
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
    padding: 20,
    alignItems: "center",
  },
  title: {
    fontSize: 22,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 20,
  },
  noData: {
    fontSize: 18,
    color: "#666",
    marginTop: 20,
  },
  card: {
    width: "100%",
    backgroundColor: "#FFF",
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 3,
  },
  productName: {
    fontSize: 18,
    fontWeight: "bold",
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

export default StatementScreen;
