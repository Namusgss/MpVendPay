



// // import React, { useState } from "react";
// // import {
// //   View,
// //   Text,
// //   StyleSheet,
// //   TextInput,
// //   TouchableOpacity,
// //   Alert,
// //   ScrollView,
// // } from "react-native";
// // import { Ionicons, FontAwesome5 } from "@expo/vector-icons";

// import React, { useState, useEffect } from "react";
// import { View, Text, TouchableOpacity, StyleSheet, Alert, ScrollView } from "react-native";
// import axios from "axios";
// import { useNavigation } from "@react-navigation/native";
// import { Ionicons,FontAwesome5 } from "@expo/vector-icons";
// import IP_ADDRESS from "../components/IPAddresses";

// // const HomeScreen = () => {
// //   const [username, setUsername] = useState(""); // Store the username
// //   const [password, setPassword] = useState(""); // Store the password
// //   const [loginData, setLoginData] = useState({ username: "", password: "" });

// const HomeScreen = ({ route }) => {
//   const navigation = useNavigation();
//   const { username } = route.params || { username: "Guest" };
//   const [balance, setBalance] = useState(0.0);

// //   // Handle Login
// //   const handleLogin = async () => {
// //     try {
// //       const response = await fetch("http://192.168.4.138:8000/login", {
// //         method: "POST",
// //         headers: {
// //           "Content-Type": "application/json",
// //         },
// //         body: JSON.stringify({
// //           username: loginData.username,
// //           password: loginData.password,
// //         }),
// //       });

// //       const data = await response.json();

// //       if (data.message === "Login successful") {
// //         setUsername(data.username); // Set username after successful login
// //       } else {
// //         Alert.alert("Error", data.detail); // Handle error
// //       }
// //     } catch (error) {
// //       console.error("Login failed:", error);
// //       Alert.alert("Error", "Failed to login");
// //     }
// //   };
//  // ✅ Fetch user balance from backend
//  useEffect(() => {
//   const fetchBalance = async () => {
//     try {
//       const response = await axios.get(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_balance`, {
//         params: { username },
//       });
//       setBalance(response.data.balance);
//     } catch (error) {
//       console.error("❌ Error fetching balance:", error);
//       Alert.alert("Error", "Could not fetch balance.");
//     }
//   };

//   fetchBalance();
// }, [username]); // ✅ Runs when `username` changes

//   // Features Row Component
//   const FeatureIcon = ({ name, icon }) => (
//     <TouchableOpacity style={styles.featureIcon}>
//       <FontAwesome5 name={icon} size={24} color="#4CAF50" />
//       <Text style={styles.featureText}>{name}</Text>
//     </TouchableOpacity>
//   );

//   // Bottom Navigation Bar
//   const NavIcon = ({ name, icon, active }) => (
//     <TouchableOpacity style={styles.navIcon}>
//       <Ionicons name={icon} size={28} color={active ? "#4CAF50" : "#aaa"} />
//       <Text style={[styles.navText, active && { color: "#4CAF50" }]}>{name}</Text>
//     </TouchableOpacity>
//   );

//   return (
//     <View style={styles.container}>
//       {/* Login Form */}
//       {!username ? (
//         <View style={styles.loginForm}>
//           <TextInput
//             style={styles.input}
//             placeholder="Username"
//             value={loginData.username}
//             onChangeText={(text) => setLoginData({ ...loginData, username: text })}
//           />
//           <TextInput
//             style={styles.input}
//             placeholder="Password"
//             secureTextEntry
//             value={loginData.password}
//             onChangeText={(text) => setLoginData({ ...loginData, password: text })}
//           />
//           <TouchableOpacity style={styles.loginButton} onPress={handleLogin}>
//             <Text style={styles.loginButtonText}>Login</Text>
//           </TouchableOpacity>
//         </View>
//       ) : (
//         <ScrollView contentContainerStyle={styles.loggedInContainer}>
//           {/* Greeting */}
//           <View style={styles.greetingContainer}>
//             <Text style={styles.greetingText}>Welcome, {username}!</Text>
//           </View>

//           {/* Features Section */}
//           <View style={styles.featuresSection}>
//             <Text style={styles.sectionTitle}>Features</Text>
//             <View style={styles.featureRow}>
//               <FeatureIcon name="Load Money" icon="wallet" />
//               <FeatureIcon name="Live Inventory" icon="mobile" />
//             </View>
//           </View>

//           {/* QR Scanner Button */}
//           <TouchableOpacity style={styles.qrScannerButton}>
//             <Ionicons name="qr-code-outline" size={32} color="#fff" />
//             <Text style={styles.qrScannerText}>Open Camera</Text>
//           </TouchableOpacity>

//           {/* Bottom Navigation */}
//           <View style={styles.bottomNav}>
//             <NavIcon name="Home" icon="home" active />
//             <NavIcon name="Statement" icon="document-text" />
//             <NavIcon name="Support" icon="help-circle" />
//             <NavIcon name="More" icon="apps" />
//           </View>
//         </ScrollView>
//       )}
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     paddingTop: 50,
//   },
//   loginForm: {
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   input: {
//     width: "80%",
//     padding: 10,
//     marginBottom: 10,
//     borderWidth: 1,
//     borderColor: "#ddd",
//     borderRadius: 5,
//   },
//   loginButton: {
//     backgroundColor: "#4CAF50",
//     padding: 10,
//     borderRadius: 5,
//     width: "80%",
//     alignItems: "center",
//   },
//   loginButtonText: {
//     color: "#fff",
//     fontSize: 16,
//   },
//   loggedInContainer: {
//     paddingHorizontal: 20,
//   },
//   greetingContainer: {
//     alignItems: "center",
//     marginBottom: 20,
//   },
//   greetingText: {
//     fontSize: 22,
//     fontWeight: "bold",
//   },
//   featuresSection: {
//     marginBottom: 20,
//   },
//   sectionTitle: {
//     fontSize: 18,
//     fontWeight: "bold",
//     marginBottom: 10,
//   },
//   featureRow: {
//     flexDirection: "row",
//     justifyContent: "space-around",
//   },
//   featureIcon: {
//     alignItems: "center",
//   },
//   featureText: {
//     fontSize: 12,
//     color: "#555",
//     marginTop: 5,
//   },
//   qrScannerButton: {
//     flexDirection: "row",
//     alignItems: "center",
//     justifyContent: "center",
//     backgroundColor: "#4CAF50",
//     padding: 10,
//     marginVertical: 20,
//     borderRadius: 10,
//   },
//   qrScannerText: {
//     color: "#fff",
//     fontSize: 16,
//     marginLeft: 10,
//   },
//   bottomNav: {
//     flexDirection: "row",
//     justifyContent: "space-around",
//     paddingVertical: 10,
//     backgroundColor: "#fff",
//     borderTopWidth: 1,
//     borderColor: "#eee",
//   },
//   navIcon: {
//     alignItems: "center",
//   },
//   navText: {
//     fontSize: 12,
//     color: "#aaa",
//   },
// });

// export default HomeScreen;

// import React, { useState, useEffect } from "react";
// import { View, Text, TouchableOpacity, StyleSheet, Alert } from "react-native";
// import axios from "axios";
// import { useNavigation } from "@react-navigation/native";
// import { Ionicons } from "@expo/vector-icons";
// import IP_ADDRESS from "../components/IPAddresses";

// const HomeScreen = ({ route }) => {
//   const navigation = useNavigation();
//   const { username } = route.params || { username: "Guest" };
//   const [balance, setBalance] = useState(0.0);

//   // ✅ Fetch user balance from backend
//   useEffect(() => {
//     const fetchBalance = async () => {
//       try {
//         const response = await axios.get(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/get_balance`, {
//           params: { username },
//         });
//         setBalance(response.data.balance);
//       } catch (error) {
//         console.error("❌ Error fetching balance:", error);
//         Alert.alert("Error", "Could not fetch balance.");
//       }
//     };

//     fetchBalance();
//   }, [username]); // ✅ Runs when `username` changes

//   return (
//     <View style={styles.container}>
//       <Text style={styles.welcomeText}>Welcome, {username}!</Text>
//       <Text style={styles.balanceText}>Your balance is: NPR{balance.toFixed(2)}</Text>

//       <TouchableOpacity style={styles.scanButton} onPress={() => navigation.navigate("ScanToPay", { username })}>
//         <Ionicons name="scan" size={28} color="#fff" />
//         <Text style={styles.buttonText}>Scan to Pay</Text>
//       </TouchableOpacity>

//       <TouchableOpacity style={styles.inventoryButton} onPress={() => navigation.navigate("Inventory")}>
//         <Ionicons name="cart" size={28} color="#fff" />
//         <Text style={styles.buttonText}>Browse Inventory</Text>
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
//   welcomeText: {
//     fontSize: 24,
//     fontWeight: "bold",
//     color: "#2E7D32",
//     marginBottom: 10,
//   },
//   balanceText: {
//     fontSize: 20,
//     fontWeight: "bold",
//     color: "#388E3C",
//     marginBottom: 30,
//   },
//   scanButton: {
//     flexDirection: "row",
//     alignItems: "center",
//     justifyContent: "center",
//     backgroundColor: "#4CAF50",
//     padding: 15,
//     width: "80%",
//     borderRadius: 10,
//     marginBottom: 20,
//   },
//   inventoryButton: {
//     flexDirection: "row",
//     alignItems: "center",
//     justifyContent: "center",
//     backgroundColor: "#2E7D32",
//     padding: 15,
//     width: "80%",
//     borderRadius: 10,
//   },
//   buttonText: {
//     color: "#fff",
//     fontSize: 18,
//     fontWeight: "bold",
//     marginLeft: 10,
//   },
// });

// export default HomeScreen;




import React, { useState, useEffect } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Alert } from "react-native";
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import IP_ADDRESS from "../components/IPAddresses";

// Define NavIcon component
const NavIcon = ({ name, icon, active, onPress }) => {
  return (
    <TouchableOpacity style={[styles.navIcon, active && styles.active]} onPress={onPress}>
      <Ionicons name={icon} size={28} color={active ? "#4CAF50" : "#888"} />
      <Text style={[styles.navIconText, active && styles.activeText]}>{name}</Text>
    </TouchableOpacity>
  );
};

const HomeScreen = ({ route }) => {
  const navigation = useNavigation();
  const { username } = route.params || { username: "Guest" };
  const [balance, setBalance] = useState(0.0);

  // Fetch user balance from backend
  useEffect(() => {
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

    fetchBalance();
  }, [username]); // Runs when `username` changes

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

      {/* Bottom Navigation */}
      <View style={styles.bottomNav}>
        <NavIcon name="Home" icon="home" active onPress={() => navigation.navigate("Home")} />
        <NavIcon name="Statement" icon="document-text" onPress={() => navigation.navigate("Statement")} />
        <NavIcon name="Support" icon="help-circle" onPress={() => navigation.navigate("Support")} />
        <NavIcon name="More" icon="apps" onPress={() => navigation.navigate("More")} />
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
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
    marginLeft: 10,
  },
  // bottomNav: {
  //   flexDirection: "row",
  //   justifyContent: "space-around",
  //   paddingVertical: 10,
  //   backgroundColor: "#fff",
  //   borderTopWidth: 1,
  //   borderColor: "#eee",
  // },
  // navIcon: {
  //   alignItems: "center",
  //   paddingVertical: 10,
  // },
  // navIconText: {
  //   fontSize: 12,
  //   color: "#888",
  // },
  // active: {
  //   backgroundColor: "#f0f0f0",
  //   borderRadius: 8,
  // },
  // activeText: {
  //   color: "#4CAF50",
  // },
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
