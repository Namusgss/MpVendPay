
import React from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
import { useRoute, useNavigation } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import NavIcon from "../components/NavIcon";

const SupportScreen = () => {
    const route = useRoute();
    const navigation = useNavigation();  
    const username = route.params?.username || "Guest";
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Support</Text>
      <Text style={styles.description}>If you need any help, contact us at support@v3ndpay.com</Text>

      {/* ✅ Working Bottom Navigation */}
      <View style={styles.bottomNav}>
        <NavIcon name="Home" icon="home" onPress={() => navigation.navigate("Home", { username })} />
        <NavIcon name="Statement" icon="document-text" onPress={() => navigation.navigate("Statement", { username })} />
        <NavIcon name="Support" icon="help-circle" active onPress={() => {}} />
        <NavIcon name="More" icon="apps" onPress={() => navigation.navigate("More", { username })} />
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

export default SupportScreen;
