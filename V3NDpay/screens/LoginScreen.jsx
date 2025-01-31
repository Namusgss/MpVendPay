// // import React, { useState } from "react";
// // import { View, Text, TextInput, TouchableOpacity, Alert, StyleSheet } from "react-native";
// // import axios from "axios";

// // const LoginScreen = ({ navigation }) => {
// //   // States for username and password
// //   const [username, setUsername] = useState("");
// //   const [password, setPassword] = useState("");

// //   // Function to handle login
// //   const handleLogin = async () => {
// //     try {
// //       const response = await axios.post("http://localhost:8000/login", {
// //         username,
// //         password,
// //       });

// //       if (response.data.message === "Login successful") {
// //         // If login is successful, navigate to home or dashboard
// //         Alert.alert("Success", "Login successful!");
// //         navigation.navigate("HomeScreen"); // Replace with your home screen name
// //       }
// //     } catch (error) {
// //       // If there's an error, show an alert with the error message
// //       if (error.response) {
// //         // Server responded with a status other than 2xx
// //         Alert.alert("Error", error.response.data.detail || "Login failed.");
// //       } else {
// //         // Network or server error
// //         Alert.alert("Error", "Something went wrong. Please try again.");
// //       }
// //     }
// //   };

// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.heading}>Login</Text>
      
// //       {/* Username input field */}
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Username"
// //         value={username}
// //         onChangeText={setUsername}
// //       />
      
// //       {/* Password input field */}
// //       <TextInput
// //         style={styles.input}
// //         placeholder="Password"
// //         secureTextEntry
// //         value={password}
// //         onChangeText={setPassword}
// //       />
      
// //       {/* Login button */}
// //       <TouchableOpacity style={styles.button} onPress={handleLogin}>
// //         <Text style={styles.buttonText}>Login</Text>
// //       </TouchableOpacity>

// //       {/* Navigation to Signup screen */}
// //       <TouchableOpacity
// //         style={styles.link}
// //         onPress={() => navigation.navigate("SignUpScreen")}
// //       >
// //         <Text>Don't have an account? Sign up</Text>
// //       </TouchableOpacity>
// //     </View>
// //   );
// // };

// // // Styling for the LoginScreen
// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     justifyContent: "center",
// //     alignItems: "center",
// //     padding: 20,
// //   },
// //   heading: {
// //     fontSize: 24,
// //     fontWeight: "bold",
// //     marginBottom: 20,
// //   },
// //   input: {
// //     width: "100%",
// //     padding: 10,
// //     marginBottom: 15,
// //     borderWidth: 1,
// //     borderColor: "#ccc",
// //     borderRadius: 5,
// //   },
// //   button: {
// //     backgroundColor: "#007bff",
// //     paddingVertical: 10,
// //     paddingHorizontal: 20,
// //     borderRadius: 5,
// //     marginBottom: 15,
// //   },
// //   buttonText: {
// //     color: "#fff",
// //     fontSize: 16,
// //   },
// //   link: {
// //     marginTop: 10,
// //   },
// // });

// // export default LoginScreen;

// import React, { useState } from 'react';
// import { View, TextInput, Button, Text, Alert, StyleSheet, TouchableOpacity} from 'react-native';
// import axios from 'axios';

// const LoginScreen = ({ navigation }) => {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');

//   const handleLogin = async () => {
//     if (!username || !password) {
//       Alert.alert('Error', 'Both fields are required!');
//       return;
//     }

//     try {
//       const response = await axios.post('http://localhost:8000/login', {
//         username,
//         password,
//       });
//       Alert.alert('Success', response.data.message);
//       navigation.navigate('Home'); // Navigate to Home after successful login
//     } catch (error) {
//       console.error('Error logging in:', error.response.data.detail || error.message);
//       Alert.alert('Error', error.response.data.detail || 'Invalid credentials');
//     }
//   };

//   return (
//         <View style={styles.container}>
//           <Text style={styles.heading}>Login</Text>
          
//           {/* Username input field */}
//           <TextInput
//             style={styles.input}
//             placeholder="Username"
//             value={username}
//             onChangeText={setUsername}
//           />
          
//           {/* Password input field */}
//           <TextInput
//             style={styles.input}
//             placeholder="Password"
//             secureTextEntry
//             value={password}
//             onChangeText={setPassword}
//           />
          
//           {/* Login button */}
//           <TouchableOpacity style={styles.button} onPress={handleLogin}>
//             <Text style={styles.buttonText}>Login</Text>
//           </TouchableOpacity>
    
//           {/* Navigation to Signup screen */}
//           <TouchableOpacity
//             style={styles.link}
//             onPress={() => navigation.navigate("SignUpScreen")}
//           >
//             <Text>Don't have an account? Sign up</Text>
//           </TouchableOpacity>
//         </View>
//       );
//     };
    
//  //Styling for the LoginScreen
// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: "center",
//     alignItems: "center",
//     padding: 20,
//   },
//   heading: {
//     fontSize: 24,
//     fontWeight: "bold",
//     marginBottom: 20,
//   },
//   input: {
//     width: "100%",
//     padding: 10,
//     marginBottom: 15,
//     borderWidth: 1,
//     borderColor: "#ccc",
//     borderRadius: 5,
//   },
//   button: {
//     backgroundColor: "#007bff",
//     paddingVertical: 10,
//     paddingHorizontal: 20,
//     borderRadius: 5,
//     marginBottom: 15,
//   },
//   buttonText: {
//     color: "#fff",
//     fontSize: 16,
//   },
//   link: {
//     marginTop: 10,
//   },
// });


// export default LoginScreen;



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

// const LoginScreen = ({ navigation }) => {
//   const [id, setId] = useState("");
//   const [password, setPassword] = useState("");
//   const [isLoading, setIsLoading] = useState(false);

//   // const handleLogin = async () => {
//   //   if (!id || !password) {
//   //     Alert.alert("Error", "Please enter both ID and password.");
//   //     return;
//   //   }

//   //   setIsLoading(true); // Start loading

//   //   try {
//   //     // API request to verify the credentials
//   //     const response = await axios.post("http://192.168.1.66:8000/login",{
//   //       password,
//   //     });

//   //     // Check if response data has the expected user credentials
//   //     if (response.data && response.data.success) {
//   //       Alert.alert("Success", "Login successful");
//   //       navigation.navigate("Home"); // Navigate to Home page
//   //     } else {
//   //       Alert.alert("Error", "Invalid ID or password.");
//   //     }
//   //   } catch (error) {
//   //     console.error("Error logging in:", error.response ? error.response.data : error.message);
//   //     Alert.alert("Error", "Network Error. Please try again.");
//   //   } finally {
//   //     setIsLoading(false); // Stop loading
//   //   }
//   // };
//   const handleLogin = async () => {
//     if (!id || !password) {
//       Alert.alert("Error", "Please enter both ID and password.");
//       return;
//     }
  
//     setIsLoading(true); // Start loading
  
//     try {
//       // API request to verify the credentials with both username and password
//       const response = await axios.post("http://192.168.1.66:8000/login", {
//         username: id,  // Sending both username and password
//         password: password,
//       });
  
//       // Check if response data has the expected success message
//       if (response.data && response.data.message === "Login successful") {
//         Alert.alert("Success", "Login successful");
//         navigation.navigate("Home"); // Navigate to Home page
//       } else {
//         Alert.alert("Error", "Invalid ID or password.");
//       }
//     } catch (error) {
//       console.error("Error logging in:", error.response ? error.response.data : error.message);
//       Alert.alert("Error", "Network Error. Please try again.");
//     } finally {
//       setIsLoading(false); // Stop loading
//     }
//   };
  

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Welcome to V3NDpay</Text>
//       <Text style={styles.subtitle}>Login to your account</Text>

//       <TextInput
//         style={styles.input}
//         placeholder="V3NDpay ID"
//         placeholderTextColor="#aaa"
//         value={id}
//         onChangeText={setId}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Password"
//         placeholderTextColor="#aaa"
//         secureTextEntry
//         value={password}
//         onChangeText={setPassword}
//       />

//       <TouchableOpacity
//         style={styles.loginButton}
//         onPress={handleLogin}
//         disabled={isLoading} // Disable the button while loading
//       >
//         <Text style={styles.loginButtonText}>
//           {isLoading ? "Logging in..." : "Login"}
//         </Text>
//       </TouchableOpacity>

//       <TouchableOpacity
//         style={styles.signUpButton}
//         onPress={() => navigation.navigate("SignUp")}
//       >
//         <Text style={styles.signUpButtonText}>Sign Up for Free</Text>
//       </TouchableOpacity>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     alignItems: "center",
//     justifyContent: "center",
//     padding: 20,
//   },
//   title: {
//     fontSize: 28,
//     fontWeight: "bold",
//     marginBottom: 10,
//     color: "#000",
//   },
//   subtitle: {
//     fontSize: 16,
//     color: "#555",
//     marginBottom: 30,
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
//   loginButton: {
//     width: "100%",
//     height: 50,
//     backgroundColor: "#4CAF50",
//     borderRadius: 8,
//     justifyContent: "center",
//     alignItems: "center",
//     marginBottom: 15,
//   },
//   loginButtonText: {
//     color: "#fff",
//     fontSize: 18,
//     fontWeight: "bold",
//   },
//   signUpButton: {
//     width: "100%",
//     height: 50,
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   signUpButtonText: {
//     color: "#4CAF50",
//     fontSize: 16,
//     fontWeight: "bold",
//   },
// });

// export default LoginScreen;



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
// import AsyncStorage from '@react-native-async-storage/async-storage';

// const LoginScreen = ({ navigation }) => {
//   const [id, setId] = useState("");
//   const [password, setPassword] = useState("");
//   const [isLoading, setIsLoading] = useState(false);

//   const handleLogin = async () => {
//     if (!id || !password) {
//       Alert.alert("Error", "Please enter both ID and password.");
//       return;
//     }

//     setIsLoading(true); // Start loading

//     try {
//       // API request to verify the credentials with both username and password
//       const response = await axios.post("http://192.168.1.66:8000/login", {
//         username: id,  // Sending both username and password
//         password: password,
//       });

//       // Check if the response contains the access token
//       if (response.data && response.data.access_token) {
//         Alert.alert("Success", "Login successful");
        
//         // Store the token securely (you can use AsyncStorage or any other secure method)
//         await AsyncStorage.setItem('token', response.data.access_token);

//         // Navigate to Home page
//         navigation.navigate("Home");
//       } else {
//         Alert.alert("Error", "Invalid ID or password.");
//       }
//     } catch (error) {
//       console.error("Error logging in:", error.response ? error.response.data : error.message);
//       Alert.alert("Error", "Network Error. Please try again.");
//     } finally {
//       setIsLoading(false); // Stop loading
//     }
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Welcome to V3NDpay</Text>
//       <Text style={styles.subtitle}>Login to your account</Text>

//       <TextInput
//         style={styles.input}
//         placeholder="V3NDpay ID"
//         placeholderTextColor="#aaa"
//         value={id}
//         onChangeText={setId}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Password"
//         placeholderTextColor="#aaa"
//         secureTextEntry
//         value={password}
//         onChangeText={setPassword}
//       />

//       <TouchableOpacity
//         style={styles.loginButton}
//         onPress={handleLogin}
//         disabled={isLoading} // Disable the button while loading
//       >
//         <Text style={styles.loginButtonText}>
//           {isLoading ? "Logging in..." : "Login"}
//         </Text>
//       </TouchableOpacity>

//       <TouchableOpacity
//         style={styles.signUpButton}
//         onPress={() => navigation.navigate("SignUp")}
//       >
//         <Text style={styles.signUpButtonText}>Sign Up for Free</Text>
//       </TouchableOpacity>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     alignItems: "center",
//     justifyContent: "center",
//     padding: 20,
//   },
//   title: {
//     fontSize: 28,
//     fontWeight: "bold",
//     marginBottom: 10,
//     color: "#000",
//   },
//   subtitle: {
//     fontSize: 16,
//     color: "#555",
//     marginBottom: 30,
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
//   loginButton: {
//     width: "100%",
//     height: 50,
//     backgroundColor: "#4CAF50",
//     borderRadius: 8,
//     justifyContent: "center",
//     alignItems: "center",
//     marginBottom: 15,
//   },
//   loginButtonText: {
//     color: "#fff",
//     fontSize: 18,
//     fontWeight: "bold",
//   },
//   signUpButton: {
//     width: "100%",
//     height: 50,
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   signUpButtonText: {
//     color: "#4CAF50",
//     fontSize: 16,
//     fontWeight: "bold",
//   },
// });

// export default LoginScreen;


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
// import AsyncStorage from '@react-native-async-storage/async-storage'; // Make sure you have this installed

// const LoginScreen = ({ navigation }) => {
//   const [username, setUsername] = useState(""); // changed from id to username
//   const [password, setPassword] = useState("");
//   const [isLoading, setIsLoading] = useState(false);

//   const handleLogin = async () => {
//     if (!username || !password) {
//       Alert.alert("Error", "Please enter both username and password.");
//       return;
//     }
//     console.log(username)
//     console.log(password)


//     setIsLoading(true); // Start loading

//     try {
//       // API request to verify the credentials
//       const response = await axios.post("http://192.168.51.241:8000/login",{
//         username,  // Pass the username here
//         password 
//       });
//       console.log(username)
//       console.log(password)
//       console.log(response)
//       // Check if response data has the expected user credentials
//       if (response.data && response.data.access_token) {
//         Alert.alert("Success", "Login successful");
        
//         // Store the JWT token in AsyncStorage
//         await AsyncStorage.setItem('access_token', response.data.access_token);

//         navigation.navigate("Home"); // Navigate to Home page
//       } else {
//         Alert.alert("Error", "Invalid username or password.");
//       }
//     } catch (error) {
//       console.error("Error logging in:", error.response ? error.response.data : error.message);
//       Alert.alert("Error", "Network Error. Please try again.");
//     } finally {
//       setIsLoading(false); // Stop loading
//     }
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Welcome to V3NDpay</Text>
//       <Text style={styles.subtitle}>Login to your account</Text>

//       <TextInput
//         style={styles.input}
//         placeholder="V3NDpay ID" // Label for username input
//         placeholderTextColor="#aaa"
//         value={username}
//         onChangeText={setUsername}
//       />
//       <TextInput
//         style={styles.input}
//         placeholder="Password"
//         placeholderTextColor="#aaa"
//         secureTextEntry
//         value={password}
//         onChangeText={setPassword}
//       />

//       <TouchableOpacity
//         style={styles.loginButton}
//         onPress={handleLogin}
//         disabled={isLoading} // Disable the button while loading
//       >
//         <Text style={styles.loginButtonText}>
//           {isLoading ? "Logging in..." : "Login"}
//         </Text>
//       </TouchableOpacity>

//       <TouchableOpacity
//         style={styles.signUpButton}
//         onPress={() => navigation.navigate("SignUp")}
//       >
//         <Text style={styles.signUpButtonText}>Sign Up for Free</Text>
//       </TouchableOpacity>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     alignItems: "center",
//     justifyContent: "center",
//     padding: 20,
//   },
//   title: {
//     fontSize: 28,
//     fontWeight: "bold",
//     marginBottom: 10,
//     color: "#000",
//   },
//   subtitle: {
//     fontSize: 16,
//     color: "#555",
//     marginBottom: 30,
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
//   loginButton: {
//     width: "100%",
//     height: 50,
//     backgroundColor: "#4CAF50",
//     borderRadius: 8,
//     justifyContent: "center",
//     alignItems: "center",
//     marginBottom: 15,
//   },
//   loginButtonText: {
//     color: "#fff",
//     fontSize: 18,
//     fontWeight: "bold",
//   },
//   signUpButton: {
//     width: "100%",
//     height: 50,
//     justifyContent: "center",
//     alignItems: "center",
//   },
//   signUpButtonText: {
//     color: "#4CAF50",
//     fontSize: 16,
//     fontWeight: "bold",
//   },
// });

// export default LoginScreen;
import React, { useState } from "react";
import { View, TextInput, Button, Alert } from "react-native";

const LoginScreen = ({ navigation, userCredentials }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    try {
      let response = await fetch("https://your-api.com/login", {
        method: "POST",
        body: formData,
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      let result = await response.json();

      if (response.ok) {
        navigation.navigate("Home");
      } else {
        Alert.alert("Error", result.message || "Login failed");
      }
    } catch (error) {
      console.error("Login error:", error);
      Alert.alert("Error", "Something went wrong");
    }
  };

  return (
    <View>
      <TextInput
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
};

export default LoginScreen;
