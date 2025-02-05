
// import React, { useState } from "react";
// import { NavigationContainer } from "@react-navigation/native";
// import { createStackNavigator } from "@react-navigation/stack";

// import LoginScreen from "./screens/LoginScreen";
// import SignUpScreen from "./screens/SignUpScreen";
// import HomeScreen from "./screens/HomeScreen";

// const Stack = createStackNavigator();

// export default function App() {
//   // Global state for storing user credentials
//   const [userCredentials, setUserCredentials] = useState(null);

//   return (
//     <NavigationContainer>
//       <Stack.Navigator initialRouteName="SignUp">
//         <Stack.Screen
//           name="SignUp"
//           options={{ headerShown: false }}
//         >
//           {(props) => (
//             <SignUpScreen
//               {...props}
//               setUserCredentials={setUserCredentials}
//             />
//           )}
//         </Stack.Screen>
//         <Stack.Screen
//           name="Login"
//           options={{ headerShown: false }}
//         >
//           {(props) => (
//             <LoginScreen {...props} userCredentials={userCredentials} />
//           )}
//         </Stack.Screen>
//         <Stack.Screen
//           name="Home"
//           component={HomeScreen}
//           options={{ headerShown: false }}
//         />
//       </Stack.Navigator>
//     </NavigationContainer>
//   );
// }


// import React, { useState } from "react";
// import { NavigationContainer } from "@react-navigation/native";
// import { createStackNavigator } from "@react-navigation/stack";

// import LoginScreen from "./screens/LoginScreen";
// import SignUpScreen from "./screens/SignUpScreen";
// import HomeScreen from "./screens/HomeScreen";
// import PaymentScreen from "./screens/PaymentScreen";
// import ScanScreen from "./screens/ScanScreen";

// const Stack = createStackNavigator();

// export default function App() {
//   // Global state for storing user credentials
//   const [userCredentials, setUserCredentials] = useState(null);

//   return (
//     <NavigationContainer>
//       <Stack.Navigator initialRouteName="SignUp">
//         <Stack.Screen
//           name="SignUp"
//           options={{ headerShown: false }}
//         >
//           {(props) => (
//             <SignUpScreen
//               {...props}
//               setUserCredentials={setUserCredentials}
//             />
//           )}
//         </Stack.Screen>
//         <Stack.Screen
//           name="Login"
//           options={{ headerShown: false }}
//         >
//           {(props) => (
//             <LoginScreen {...props} userCredentials={userCredentials} />
//           )}
//         </Stack.Screen>
//         <Stack.Screen
//           name="Home"
//           component={HomeScreen}
//           options={{ headerShown: false }}
//         />
//         <Stack.Screen name="ScanToPay" component={ScanScreen} options={{ headerShown: false }} />

//         <Stack.Screen name="PaymentScreen" component={PaymentScreen} options={{ headerShown: false }} />

//       </Stack.Navigator>
//     </NavigationContainer>
//   );
// }


// import React, { useState } from "react";
// import { NavigationContainer } from "@react-navigation/native";
// import { createStackNavigator } from "@react-navigation/stack";

// import LoginScreen from "./screens/LoginScreen";
// import SignUpScreen from "./screens/SignUpScreen";
// import HomeScreen from "./screens/HomeScreen";
// import PaymentScreen from "./screens/PaymentScreen";
// import ScanScreen from "./screens/ScanScreen";
// import StatementScreen from "./screens/StatementScreen";

// const Stack = createStackNavigator();

// export default function App() {
//   // Global state for storing user credentials
//   const [userCredentials, setUserCredentials] = useState(null);

//   return (
//     <NavigationContainer>
//       <Stack.Navigator initialRouteName="SignUp">
//         <Stack.Screen
//           name="SignUp"
//           options={{ headerShown: false }}
//         >
//           {(props) => (
//             <SignUpScreen
//               {...props}
//               setUserCredentials={setUserCredentials}
//             />
//           )}
//         </Stack.Screen>
//         <Stack.Screen
//           name="Login"
//           options={{ headerShown: false }}
//         >
//           {(props) => (
//             <LoginScreen {...props} userCredentials={userCredentials} />
//           )}
//         </Stack.Screen>
//         <Stack.Screen
//           name="Home"
//           component={HomeScreen}
//           options={{ headerShown: false }}
//         />
//         <Stack.Screen name="ScanToPay" component={ScanScreen} options={{ headerShown: false }} />

//         <Stack.Screen name="PaymentScreen" component={PaymentScreen} options={{ headerShown: false }} />

//         <Stack.Screen name="Statement" component={StatementScreen} />

//       </Stack.Navigator>
//     </NavigationContainer>
//   );
// }


import React, { useState, useEffect } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import LoginScreen from "./screens/LoginScreen";
import SignUpScreen from "./screens/SignUpScreen";
import HomeScreen from "./screens/HomeScreen";
import PaymentScreen from "./screens/PaymentScreen";
import ScanScreen from "./screens/ScanScreen";
import StatementScreen from "./screens/StatementScreen";
import SupportScreen from "./screens/SupportScreen"; // Import the screen
import MoreScreen from "./screens/MoreScreen";

const Stack = createStackNavigator();

export default function App() {
  // Global state for storing user credentials
  const [userCredentials, setUserCredentials] = useState(null);

  useEffect(() => {
    // Check if user credentials are available and navigate to Home screen
    if (userCredentials) {
      navigation.navigate("Home", { username: userCredentials.username });
    }
  }, [userCredentials]);

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
            <LoginScreen {...props} setUserCredentials={setUserCredentials} />
          )}
        </Stack.Screen>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen name="ScanToPay" component={ScanScreen} options={{ headerShown: false }} />
        <Stack.Screen name="PaymentScreen" component={PaymentScreen} options={{ headerShown: false }} />
        
        <Stack.Screen name="Statement" component={StatementScreen}initialParams={{ username: userCredentials?.username }}/>
        <Stack.Screen name="Support" component={SupportScreen} />
        <Stack.Screen name="More" component={ MoreScreen} />

      </Stack.Navigator>
    </NavigationContainer>
  );
}
