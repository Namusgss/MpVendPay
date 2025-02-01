
import React, { useState } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import LoginScreen from "./screens/LoginScreen";
import SignUpScreen from "./screens/SignUpScreen";
import HomeScreen from "./screens/HomeScreen";
import PaymentScreen from "./screens/PaymentScreen";
import ScanScreen from "./screens/ScanScreen";

const Stack = createStackNavigator();

export default function App() {
  // Global state for storing user credentials
  const [userCredentials, setUserCredentials] = useState(null);

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="SignUp">
        <Stack.Screen
          name="SignUp"
          options={{ headerShown: false }}
        >
          {(props) => (
            <SignUpScreen
              {...props}
              setUserCredentials={setUserCredentials}
            />
          )}
        </Stack.Screen>
        <Stack.Screen
          name="Login"
          options={{ headerShown: false }}
        >
          {(props) => (
            <LoginScreen {...props} userCredentials={userCredentials} />
          )}
        </Stack.Screen>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen name="ScanToPay" component={ScanScreen} options={{ headerShown: false }} />

        <Stack.Screen name="PaymentScreen" component={PaymentScreen} options={{ headerShown: false }} />

      </Stack.Navigator>
    </NavigationContainer>
  );
}
