
// import React, { useEffect, useState } from "react";
// import { View, Text, FlatList, StyleSheet, ActivityIndicator, Alert } from "react-native";
// import { useRoute, useNavigation} from "@react-navigation/native";
// import IP_ADDRESS from "../components/IPAddresses";
// import NavIcon from "../components/NavIcon";

// const StatementScreen = () => {
//   const route = useRoute();
//   const navigation = useNavigation();  
//   const username = route.params?.username || "Guest"; // Fallback if username is not available
//   console.log("Username in StatementScreen:", username);

//   const [history, setHistory] = useState([]);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     // Ensure username is available before fetching data
//     if (username && username !== "Guest") {
//       console.log("Fetching purchase history for:", username);
//       fetch(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_purchase_history?username=${username}`)
//         .then((response) => response.json())
//         .then((data) => {
//           // Check for empty response
//           setHistory(data.message ? [] : data);
//           setLoading(false);
//         })
//         .catch((error) => {
//           console.error("Error fetching history:", error);
//           setLoading(false);
//           Alert.alert("Error", "Failed to fetch purchase history. Please try again.");
//         });
//     } else {
//       setLoading(false);
//     }
//   }, [username]);

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Purchase History for {username}</Text>
//       {loading ? (
//         <ActivityIndicator size="large" color="#2E7D32" />
//       ) : history.length === 0 ? (
//         <Text style={styles.noData}>No transactions found.</Text>
//       ) : (
//         <FlatList
//           data={history}
//           keyExtractor={(item, index) => index.toString()}
//           renderItem={({ item }) => (
//             <View style={styles.card}>
//               <Text style={styles.productName}>{item.productName}</Text>
//               <Text>Quantity: {item.quantity}</Text>
//               <Text>Amount: NPR {item.amount}</Text>
//             </View>
//           )}
//         />
//       )}
//       <View style={styles.bottomNav}>
//         <NavIcon name="Home" icon="home" onPress={() => navigation.navigate("Home", { username })} />
//         <NavIcon name="Statement" icon="document-text" active onPress={() => {}} />
//         <NavIcon name="Support" icon="help-circle" onPress={() => navigation.navigate("Support", { username })} />
//         <NavIcon name="More" icon="apps" onPress={() => navigation.navigate("More", { username })} />
//       </View>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#E8F5E9",
//     padding: 20,
//     alignItems: "center",
//   },
//   title: {
//     fontSize: 22,
//     fontWeight: "bold",
//     color: "#2E7D32",
//     marginBottom: 20,
//   },
//   noData: {
//     fontSize: 18,
//     color: "#666",
//     marginTop: 20,
//   },
//   card: {
//     width: "100%",
//     backgroundColor: "#FFF",
//     padding: 15,
//     borderRadius: 10,
//     marginBottom: 10,
//     shadowColor: "#000",
//     shadowOpacity: 0.1,
//     shadowRadius: 5,
//     elevation: 3,
//   },
//   productName: {
//     fontSize: 18,
//     fontWeight: "bold",
//   },
  
//   bottomNav: {
//     flexDirection: "row",
//     justifyContent: "space-around",
//     paddingVertical: 10,
//     backgroundColor: "#fff",
//     borderTopWidth: 1,
//     borderColor: "#eee",
//     position: "absolute", // Pin the bottom navigation to the bottom
//     bottom: 0,
//     left: 0,
//     right: 0,
//   },
//   navIcon: {
//     alignItems: "center",
//   },
//   navText: {
//     fontSize: 12,
//     color: "#aaa",
//   },
// });

// export default StatementScreen;

import React, { useEffect, useState } from "react";
import { View, Text, FlatList, StyleSheet, ActivityIndicator, Alert, TouchableOpacity } from "react-native";
import { useRoute, useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import IP_ADDRESS from "../components/IPAddresses";
import NavIcon from "../components/NavIcon";
 
const StatementScreen = () => {
  const route = useRoute();
  const navigation = useNavigation();
  const username = route.params?.username || "Guest";
 
  const [history, setHistory] = useState([]);
  const [balance, setBalance] = useState(0);
  const [loading, setLoading] = useState(true);
  const [selectedFilter, setSelectedFilter] = useState("7 days");
 
  useEffect(() => {
    if (username && username !== "Guest") {
      fetchBalance();
      fetchPurchaseHistory();
    } else {
      setLoading(false);
    }
  }, [username]);
 
  const fetchBalance = () => {
    fetch(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_balance?username=${username}`)
      .then((response) => response.json())
      .then((data) => {
        setBalance(data.balance || 0);
      })
      .catch((error) => {
        console.error("Error fetching balance:", error);
        Alert.alert("Error", "Failed to fetch balance.");
      });
  };
 
  const fetchPurchaseHistory = () => {
    fetch(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_purchase_history?username=${username}`)
      .then((response) => response.json())
      .then((data) => {
        setHistory(data.message ? [] : data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching history:", error);
        setLoading(false);
        Alert.alert("Error", "Failed to fetch purchase history.");
      });
  };
 
  return (
    <View style={styles.container}>
      {/* Green Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Statement</Text>
        <View style={styles.balanceContainer}>
          <Ionicons name="wallet-outline" size={20} color="#fff" />
          <Text style={styles.balanceText}>NPR {balance.toFixed(2)}</Text>
        </View>
      </View>
 
      {/* Transaction List */}
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
              <Ionicons name={item.amount > 0 ? "arrow-up-circle" : "arrow-down-circle"} size={24} color={item.amount > 0 ? "green" : "red"} />
              <View style={styles.cardContent}>
                <Text style={styles.productName}>{item.productName}</Text>
                <Text style={styles.transactionDetails}>Quantity: {item.quantity}</Text>
                <Text style={styles.transactionDetails}>Amount: NPR {item.amount}</Text>
                <Text style={styles.transactionDate}>Date: {item.transactionDate}</Text>
                <Text style={styles.transactionTime}>Time: {item.transactionTime}</Text>
              </View>
            </View>
          )}
        />
      )}
 
      {/* Bottom Navigation */}
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
    backgroundColor: "#F5F5F5",
  },
  header: {
    backgroundColor: "#2E7D32",
    paddingVertical: 20,
    paddingHorizontal: 20,
    alignItems: "center",
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#fff",
  },
  balanceContainer: {
    flexDirection: "row",
    alignItems: "center",
    marginTop: 5,
  },
  balanceText: {
    fontSize: 16,
    color: "#fff",
    marginLeft: 5,
  },
  filterContainer: {
    flexDirection: "row",
    justifyContent: "center",
    marginVertical: 10,
  },
  filterButton: {
    paddingVertical: 8,
    paddingHorizontal: 15,
    borderRadius: 20,
    marginHorizontal: 5,
    backgroundColor: "#E0E0E0",
  },
  activeFilter: {
    backgroundColor: "#2E7D32",
  },
  filterText: {
    fontSize: 14,
    color: "#666",
  },
  activeFilterText: {
    color: "#fff",
  },
  noData: {
    fontSize: 18,
    color: "#666",
    textAlign: "center",
    marginTop: 20,
  },
  card: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "#FFF",
    padding: 15,
    borderRadius: 10,
    marginHorizontal: 10,
    marginVertical: 5,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 3,
  },
  cardContent: {
    flex: 1,
    marginLeft: 10,
  },
  productName: {
    fontSize: 16,
    fontWeight: "bold",
  },
  transactionDetails: {
    fontSize: 14,
    color: "#666",
  },
  transactionDate: {
    fontSize: 12,
    color: "#666",
    marginTop: 5,
  },
  transactionTime: {
    fontSize: 12,
    color: "#666",
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
 
export default StatementScreen;