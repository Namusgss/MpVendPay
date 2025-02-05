
import React, { useState } from "react";
import { View, TextInput, Button, Alert,Text, TouchableOpacity } from "react-native";
import { SafeAreaView, StyleSheet } from "react-native";
import axios from "axios";
import IP_ADDRESS from "../components/IPAddresses";  // Ensure this is correctly imported



const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);


const handleLogin = async () => {
  if (!username || !password) {
    Alert.alert("Error", "All fields are required.");
    return;
  }

  try {
    const response = await axios.post(
      `${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/login`,
      {
        username: username.trim(),  // ✅ Ensure correct username format
        password: password,
      },
      {
        headers: { "Content-Type": "application/json" },
      }
    );

    console.log("✅ Login Success:", response.data);

    Alert.alert("Success", "Login successful!");
    navigation.navigate("Home", { username: username.trim() });  // ✅ Ensure username is passed correctly

  } catch (error) {
    console.error("❌ Login Error:", error);

    let errorMessage = "Login failed.";
    if (error.response) {
      errorMessage = error.response.data?.detail || error.response.data?.message || errorMessage;
    }

    Alert.alert("Error", errorMessage);
  }
};
  return (
  <View style={styles.container}>
    <Text style={styles.title}>Welcome to V3NDpay</Text>
    <Text style={styles.subtitle}>Login to your account</Text>

    <TextInput
      style={styles.input}
      placeholder="V3NDpay ID" // Label for username input
      placeholderTextColor="#aaa"
      value={username}
      onChangeText={setUsername}
    />
    <TextInput
      style={styles.input}
      placeholder="Password"
      placeholderTextColor="#aaa"
      secureTextEntry
      value={password}
      onChangeText={setPassword}
    />

    <TouchableOpacity
      style={styles.loginButton}
      onPress={handleLogin}
      disabled={isLoading} // Disable the button while loading
    >
      <Text style={styles.loginButtonText}>
        {isLoading ? "Logging in..." : "Login"}
      </Text>
    </TouchableOpacity>

    <TouchableOpacity
      style={styles.signUpButton}
      onPress={() => navigation.navigate("SignUp")}
    >
      <Text style={styles.signUpButtonText}>Sign Up for Free</Text>
    </TouchableOpacity>
  </View>
  );
};

const styles = StyleSheet.create({
container: {
  flex: 1,
  backgroundColor: "#fff",
  alignItems: "center",
  justifyContent: "center",
  padding: 20,
},
title: {
  fontSize: 28,
  fontWeight: "bold",
  marginBottom: 10,
  color: "#000",
},
subtitle: {
  fontSize: 16,
  color: "#555",
  marginBottom: 30,
},
input: {
  width: "100%",
  height: 50,
  backgroundColor: "#f5f5f5",
  borderRadius: 8,
  paddingHorizontal: 15,
  marginBottom: 15,
  fontSize: 16,
},
loginButton: {
  width: "100%",
  height: 50,
  backgroundColor: "#4CAF50",
  borderRadius: 8,
  justifyContent: "center",
  alignItems: "center",
  marginBottom: 15,
},
loginButtonText: {
  color: "#fff",
  fontSize: 18,
  fontWeight: "bold",
},
signUpButton: {
  width: "100%",
  height: 50,
  justifyContent: "center",
  alignItems: "center",
},
signUpButtonText: {
  color: "#4CAF50",
  fontSize: 16,
  fontWeight: "bold",
},
});


export default LoginScreen;


