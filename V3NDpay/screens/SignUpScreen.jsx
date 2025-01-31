// // import React from "react";
// // import {
// //   View,
// //   Text,
// //   TouchableOpacity,
// //   TextInput,
// //   StyleSheet,
// // } from "react-native";

// // const SignUpScreen = ({ navigation }) => {
// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.title}>Create Your V3NDpay Account</Text>

// //       <TextInput
// //         style={styles.input}
// //         placeholder="Full Name"
// //         placeholderTextColor="#aaa"
// //       />
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Email"
// //         placeholderTextColor="#aaa"
// //         keyboardType="email-address"
// //       />
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Password"
// //         placeholderTextColor="#aaa"
// //         secureTextEntry
// //       />
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Confirm Password"
// //         placeholderTextColor="#aaa"
// //         secureTextEntry
// //       />

// //       <TouchableOpacity
// //         style={styles.signUpButton}
// //         onPress={() => navigation.navigate("Login")}
// //       >
// //         <Text style={styles.signUpButtonText}>Sign Up</Text>
// //       </TouchableOpacity>

// //       <TouchableOpacity
// //         style={styles.backButton}
// //         onPress={() => navigation.navigate("Login")}
// //       >
// //         <Text style={styles.backButtonText}>Back to Login</Text>
// //       </TouchableOpacity>
// //     </View>
// //   );
// // };

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     backgroundColor: "#fff",
// //     alignItems: "center",
// //     justifyContent: "center",
// //     padding: 20,
// //   },
// //   title: {
// //     fontSize: 24,
// //     fontWeight: "bold",
// //     marginBottom: 20,
// //     color: "#000",
// //   },
// //   input: {
// //     width: "100%",
// //     height: 50,
// //     backgroundColor: "#f5f5f5",
// //     borderRadius: 8,
// //     paddingHorizontal: 15,
// //     marginBottom: 15,
// //     fontSize: 16,
// //   },
// //   signUpButton: {
// //     width: "100%",
// //     height: 50,
// //     backgroundColor: "#4CAF50",
// //     borderRadius: 8,
// //     justifyContent: "center",
// //     alignItems: "center",
// //     marginBottom: 15,
// //   },
// //   signUpButtonText: {
// //     color: "#fff",
// //     fontSize: 18,
// //     fontWeight: "bold",
// //   },
// //   backButton: {
// //     justifyContent: "center",
// //     alignItems: "center",
// //   },
// //   backButtonText: {
// //     color: "#4CAF50",
// //     fontSize: 16,
// //     fontWeight: "bold",
// //   },
// // });

// // export default SignUpScreen;
// import React, { useState } from "react";
// import {
//   View,
//   Text,
//   TouchableOpacity,
//   TextInput,
//   StyleSheet,
//   Alert,
// } from "react-native";
// import axios from "axios";

// const SignUpScreen = ({ navigation }) => {
//   // State hooks for form inputs
//   const [fullName, setFullName] = useState("");
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [confirmPassword, setConfirmPassword] = useState("");
//   const [number, setNumber] = useState("");

//   // Handle sign-up action
//   const handleSignUp = async () => {
//     // Validation checks for empty fields
//     if (!fullName || !email || !password || !confirmPassword || !number) {
//       Alert.alert("Error", "Please fill in all fields.");
//       return;
//     }

//     // Check if passwords match
//     if (password !== confirmPassword) {
//       Alert.alert("Error", "Passwords do not match.");
//       return;
//     }

//     try {
//       // Replace localhost with your local IP address (e.g., 192.168.x.x:8000)
//       const response = await axios.post(" http://192.168.72.241:8000/register", {
//         username: fullName,
//         email: email,
//         password: password,
//         number: number
//       });

//       // Show success message and navigate to login page
//       Alert.alert("Success", response.data.message);
//       navigation.navigate("Login"); // Navigate to Login screen after successful signup
//     } catch (error) {
//       console.error(error);
//       Alert.alert("Error", error.response?.data?.detail || "An error occurred");
//     }
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Create Your V3NDpay Account</Text>

//       {/* Full Name Input */}
//       <TextInput
//         style={styles.input}
//         placeholder="Full Name"
//         placeholderTextColor="#aaa"
//         value={fullName}
//         onChangeText={setFullName}
//       />

//       {/* Email Input */}
//       <TextInput
//         style={styles.input}
//         placeholder="Email"
//         placeholderTextColor="#aaa"
//         keyboardType="email-address"
//         value={email}
//         onChangeText={setEmail}
//       />

//       {/* Password Input */}
//       <TextInput
//         style={styles.input}
//         placeholder="Password"
//         placeholderTextColor="#aaa"
//         secureTextEntry
//         value={password}
//         onChangeText={setPassword}
//       />

//       {/* Confirm Password Input */}
//       <TextInput
//         style={styles.input}
//         placeholder="Confirm Password"
//         placeholderTextColor="#aaa"
//         secureTextEntry
//         value={confirmPassword}
//         onChangeText={setConfirmPassword}
//       />

//       {/* Phone Number Input */}
//       <TextInput
//         style={styles.input}
//         placeholder="Phone Number"
//         placeholderTextColor="#aaa"
//         keyboardType="phone-pad"
//         value={number}
//         onChangeText={setNumber}
//       />

//       {/* Sign Up Button */}
//       <TouchableOpacity
//         style={styles.signUpButton}
//         onPress={handleSignUp}
//       >
//         <Text style={styles.signUpButtonText}>Sign Up</Text>
//       </TouchableOpacity>

//       {/* Back to Login Button */}
//       <TouchableOpacity
//         style={styles.backButton}
//         onPress={() => navigation.navigate("Login")}
//       >
//         <Text style={styles.backButtonText}>Back to Login</Text>
//       </TouchableOpacity>
//     </View>
//   );
// };

// // StyleSheet for the SignUpScreen
// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     alignItems: "center",
//     justifyContent: "center",
//     padding: 20,
//   },
//   title: {
//     fontSize: 24,
//     fontWeight: "bold",
//     marginBottom: 20,
//     color: "#000",
//   },
//   input: {
//     width: "100%",
//     height: 50,
//     backgroundColor: "#f5f5f5",
//     borderRadius: 8,
//     paddingHorizontal: 15,
//     marginBottom: 15,
//     fontSize: 16,
//   },
//   signUpButton: {
//     width: "100%",
//     height: 50,
//     backgroundColor: "#4CAF50",
//     borderRadius: 8,
//     justifyContent: "center",
//     alignItems: "center",
//     marginBottom: 15,
//   },
//   signUpButtonText: {
//     color: "#fff",
//     fontSize: 18,
//     fontWeight: "bold",
//   },
//   backButton: {
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   backButtonText: {
//     color: "#4CAF50",
//     fontSize: 16,
//     fontWeight: "bold",
//   },
// });

// export default SignUpScreen;

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

const SignUpScreen = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [number, setNumber] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSignUp = async () => {
    if (!username || !password || !email || !number) {
      Alert.alert("Error", "All fields are required.");
      return;
    }

    setIsLoading(true); // Start loading

    try {
      const response = await axios.post("http://192.168.72.241:8000/register", {
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
