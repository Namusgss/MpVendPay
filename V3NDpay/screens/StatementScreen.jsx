import React, { useEffect, useState } from "react";
import { View, Text, FlatList, StyleSheet, ActivityIndicator } from "react-native";
import IP_ADDRESS from "../components/IPAddresses";
// import { useUser } from "../UserContext"; // Import user context

const StatementScreen = () => {
  const { username } = useUser(); // Get logged-in username
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (username) {
      fetch(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_purchase_history?username=${username}`)
        .then((response) => response.json())
        .then((data) => {
          setHistory(data.message ? [] : data);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error fetching history:", error);
          setLoading(false);
        });
    }
  }, [username]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Purchase History</Text>
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
});

export default StatementScreen;
