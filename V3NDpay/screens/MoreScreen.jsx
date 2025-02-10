// import React from "react";
// import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
// import { useRoute, useNavigation } from "@react-navigation/native";
// import NavIcon from "../components/NavIcon";
// import IP_ADDRESS from "../components/IPAddresses";
// import axios from "axios"; // Correct way to import axios

// const MoreScreen = () => {
//    const route = useRoute();
//       const navigation = useNavigation();  
//       const username = route.params?.username || "Guest";

//   const handleLogout = () => {
//     // Clear user data here if necessary (e.g., remove tokens, clear local storage, etc.)
//     navigation.navigate("Login"); // Navigate to the login screen
//   };

  

//   const handleAboutUs = () => {
//     // Navigate to the About Us screen
//     navigation.navigate("AboutUs");
//   };

//   return (
//     <View style={styles.container}>

//       {/* About Us Section */}
//       <TouchableOpacity style={styles.button} onPress={handleAboutUs}>
//         <Text style={styles.buttonText}>About Us</Text>
//       </TouchableOpacity>

//       {/* Logout Section */}
//       <TouchableOpacity style={styles.button} onPress={handleLogout}>
//         <Text style={styles.buttonText}>Logout</Text>
//       </TouchableOpacity>

//       {/* Bottom Navigation */}
//       <View style={styles.bottomNav}>
//         <NavIcon name="Home" icon="home" onPress={() => navigation.navigate("Home", { username })} />
//         <NavIcon name="Statement" icon="document-text" onPress={() => navigation.navigate("Statement", { username })} />
//         <NavIcon name="Support" icon="help-circle" onPress={() => navigation.navigate("Support", { username })} />
//         <NavIcon name="More" icon="apps" active onPress={() => {}} />
//       </View>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//     container: {
//       flex: 1,
//       justifyContent: "center",
//       alignItems: "center",
//       backgroundColor: "#E8F5E9",
//       padding: 20,
//     },
//     title: {
//       fontSize: 24,
//       fontWeight: "bold",
//       color: "#2E7D32",
//       marginBottom: 10,
//     },
//     description: {
//       fontSize: 16,
//       color: "#555",
//       textAlign: "center",
//       marginBottom: 20,
//     },
//     button: {
//       flexDirection: "row",
//       alignItems: "center",
//       backgroundColor: "#4CAF50",
//       padding: 12,
//       borderRadius: 10,
//       marginTop: 20,
//     },
//     buttonText: {
//       color: "#fff",
//       fontSize: 18,
//       fontWeight: "bold",
//       marginLeft: 10,
//     },
//     bottomNav: {
//       flexDirection: "row",
//       justifyContent: "space-around",
//       paddingVertical: 10,
//       backgroundColor: "#fff",
//       borderTopWidth: 1,
//       borderColor: "#eee",
//       position: "absolute", // Pin the bottom navigation to the bottom
//       bottom: 0,
//       left: 0,
//       right: 0,
//     },
//     navIcon: {
//       alignItems: "center",
//     },
//     navText: {
//       fontSize: 12,
//       color: "#aaa",
//     },
//   });
  

// export default MoreScreen;

import React from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
import { useRoute, useNavigation } from "@react-navigation/native";
import NavIcon from "../components/NavIcon";

const MoreScreen = () => {
  const route = useRoute();
  const navigation = useNavigation();  
  const username = route.params?.username || "Guest";  // Accessing the username from params
  
  const handleLogout = () => {
    // Here, we're navigating to the login screen and clearing the username from params
    navigation.reset({
      index: 0,
      routes: [{ name: "Login" }],  // Reset the navigation stack to just the login screen
    });
  };

  const handleAboutUs = () => {
    // Navigate to the About Us screen
    navigation.navigate("AboutUs");
  };

  return (
    <View style={styles.container}>
      {/* About Us Section */}
      <TouchableOpacity style={styles.button} onPress={handleAboutUs}>
        <Text style={styles.buttonText}>About Us</Text>
      </TouchableOpacity>

      {/* Logout Section */}
      <TouchableOpacity style={styles.button} onPress={handleLogout}>
        <Text style={styles.buttonText}>Logout</Text>
      </TouchableOpacity>

      {/* Bottom Navigation */}
      <View style={styles.bottomNav}>
        <NavIcon name="Home" icon="home" onPress={() => navigation.navigate("Home", { username })} />
        <NavIcon name="Statement" icon="document-text" onPress={() => navigation.navigate("Statement", { username })} />
        <NavIcon name="Support" icon="help-circle" onPress={() => navigation.navigate("Support", { username })} />
        <NavIcon name="More" icon="apps" active onPress={() => {}} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#E8F5E9",
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#2E7D32",
    marginBottom: 10,
  },
  description: {
    fontSize: 16,
    color: "#555",
    textAlign: "center",
    marginBottom: 20,
  },
  button: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "#4CAF50",
    padding: 12,
    borderRadius: 10,
    marginTop: 20,
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

export default MoreScreen;
