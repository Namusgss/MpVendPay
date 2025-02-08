
import React, { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
  StyleSheet,
  Alert,
} from "react-native";
import axios from "axios";
import IP_ADDRESS from "../components/IPAddresses";

const SignUpScreen = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [number, setNumber] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  // Password validation: Minimum 8 characters, at least 1 uppercase, 1 number
  const validatePassword = (password) => {
    return /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/.test(password);
  };

  const handleSignUp = async () => {
    if (!username || !password || !email || !number) {
      Alert.alert("Error", "All fields are required.");
      return;
    }

    if (!validatePassword(password)) {
      Alert.alert("Error", "Password must be at least 8 characters long, contain at least 1 uppercase letter, and 1 number.");
      return;
    }

    setIsLoading(true); // Start loading

    try {
      const response = await axios.post(`${IP_ADDRESS.LOCAL_IP}:${IP_ADDRESS.LOCAL_PORT}/register`, {
        username,
        password,
        email,
        number,
      });

      if (response.data) {
        Alert.alert("Success", "User registered successfully.");
        navigation.navigate("Login");
      }
    } catch (error) {
      console.error("Error during sign-up:", error);
      if (error.response) {
        Alert.alert("Error", error.response.data.detail || "Sign-up failed.");
      } else {
        Alert.alert("Error", "Network Error. Please check your connection.");
      }
    } finally {
      setIsLoading(false); // Stop loading
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Create an Account</Text>

      <TextInput
        style={styles.input}
        placeholder="Username"
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
      <TextInput
        style={styles.input}
        placeholder="Email"
        placeholderTextColor="#aaa"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Phone Number"
        placeholderTextColor="#aaa"
        value={number}
        onChangeText={setNumber}
      />

      <TouchableOpacity
        style={styles.signUpButton}
        onPress={handleSignUp}
        disabled={isLoading}
      >
        <Text style={styles.signUpButtonText}>
          {isLoading ? "Signing Up..." : "Sign Up"}
        </Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.loginButton}
        onPress={() => navigation.navigate("Login")}
      >
        <Text style={styles.loginButtonText}>Already have an account? Login</Text>
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
  input: {
    width: "100%",
    height: 50,
    backgroundColor: "#f5f5f5",
    borderRadius: 8,
    paddingHorizontal: 15,
    marginBottom: 15,
    fontSize: 16,
  },
  signUpButton: {
    width: "100%",
    height: 50,
    backgroundColor: "#4CAF50",
    borderRadius: 8,
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 15,
  },
  signUpButtonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
  },
  loginButton: {
    width: "100%",
    height: 50,
    justifyContent: "center",
    alignItems: "center",
  },
  loginButtonText: {
    color: "#4CAF50",
    fontSize: 16,
    fontWeight: "bold",
  },
});

export default SignUpScreen;
