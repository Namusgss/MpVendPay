import React, { useState } from "react";
import { View, TextInput, Button, Alert } from "react-native";
import { SafeAreaView, StyleSheet } from "react-native";
import axios from "axios";
import IP_ADDRESS from "../components/IPAddresses";  // Ensure this is correctly imported

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

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
    <SafeAreaView style={styles.container}>
      <TextInput
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        style={styles.input}
      />
      <TextInput
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
        style={styles.input}
      />
      <Button title="Login" onPress={handleLogin} />
    </SafeAreaView>
  );
};

export default LoginScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
  },
  input: {
    height: 50,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 10,
    marginBottom: 15,
    paddingHorizontal: 10,
  },
});
