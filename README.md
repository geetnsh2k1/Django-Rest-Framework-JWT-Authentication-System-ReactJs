# Django Rest Framework JWT Authentication System - ReactJs

## Introduction

> This is an implementation of an authentication system using JSON Web Token (JWT) for authorization and authentication.

## Authentication V/S Authorization

> Authentication and authorization are the two words used in the security world. They might sound similar but are completely different from each other. Authentication is used to authenticate someone's identity, whereas authorization is a way to provide permission to someone to access a particular resource. In layman language, Authentication verifies the user's identity, and Authorization verifies the user's access and permissions. If the user can't prove their identity, they cannot access the system. And if you are authenticated by proving the correct identity, but you are not authorized to perform a specific function, you won't be able to access that. However, both security methods are often used together.

## About JWT

> JSON Web Tokens are used to authenticate and authorize the user. It is an open standard and compact mechanism for transmitting data across the server. It plays an important role in securely transmitting the data using the JSON object. JWT architecture uses two types of tokens for the working, mainly known as Access Tokens and Refresh Tokens. Read further about JWT from https://jwt.io/introduction/

## Django Rest Framework

> Django Rest Framework, better known as DRF is a powerful and flexible toolkit for building Web APIs. DRF provides a lot of features to a developer. DRF is easy to use, customizable, pluggable, and serializable. You can read further about DRF from their official documentation https://www.django-rest-framework.org/

## Access Tokens

> Access tokens are credentials used to access protected resources.
 
Access tokens are used as bearer tokens. A bearer token means that the bearer (who holds the access token) can access authorized resources without further identification.
 
Because of this, it is important that bearer tokens be protected.
 
These tokens usually have a short lifespan for security purpose. When it expires, the user must authenticate again to get a new access token limiting the exposure of the fact that it is a bearer token.
 
Access token must never be used for authentication. Access tokens cannot tell if the user has authenticated. The only user information the access token processes is the user id, located in sub claims.
 
The application receives an access token after a user successfully authenticates and authorizes access. Itis usually in JWT format but do not have to be.

** An access token is put in the Authorization header of your request, usually looks like Bearer “access_token” that the API you are calling can verify and grant you access.

## Why do we need Access Token?

> Access tokens are used to inform an API that the bearer of the token has been authorized to access the API and perform a predetermined set of actions specified by the scope. It is used to authorize API access.

## Refresh Tokens

> This token is a long-lived token compared to the access token and is used to request a new access token in cases where it is expired. It can be considered as credentials used to obtain access tokens. It's allowed for long-lived access and highly confidential. Refresh tokens can be used for grant types – authorization code and password credentials grant. Refresh tokens are intended for use only with authorization servers and are never sent to resource servers. You will receive this in an encoded format only that cannot be decoded. An example could be 494c427ace9e04dea03c7234cea96c5ca53e0ce4ea95147e961fd9ebcf8feb84

## Why do we need Refresh Token?

> As access token has defined lifetimes, and there could be a possibility that the current access token becomes invalid or expires. This is the token used to request new access tokens without user interaction.

## Where to store Access Tokens and Refresh Tokens?

> One of the hardest parts of the JWT implemention is to crack that where it is safe to store access token and refresh token. 

** Which is the best policy LocalStorage? SessionStorage? Cookies? Variable?

First of all, let's talk about storing the token at local storage. It’s pure JavaScript and it’s convenient. If you don’t have a back-end and you’re relying on a third-party API, you can’t always ask the third-party API to set a specific cookie for your site. But, one can access the token using vanilla javascript. Therefore, an XSS attack happens when an attacker can run JavaScript on your website. This means that the attacker can take the access token that you stored in your localStorage. An XSS attack can happen from a third-party JavaScript code included in your website like React, Vue, jQuery, Google Analytics, etc. It's almost impossible not to include any third-party libraries in your site. Therefore, considering the situation storing token in local storage is not a good idea.

Now, let's continue with session storage. This is almost identical to local storage, with one important difference: session storage does not persist across browsing contexts, meaning it is destroyed if you close the page. The only difference between local storage and session storage is persistence. If you close the window or open a new one, the token value will disappear from session storage, as opposed to local storage. Therefore, just like with local storage, session storage offers zero protection against XSS, since it is designed to be read and write from JavaScript.

Now, let's talk about cookies. This is considered as the best practice to store tokens. We can use httpOnly enabled cookies to store tokens. That is if we are using httpOnly and secure cookies this means that your cookies cannot be accessed using JavaScript so even if an attacker can run JS on your site, they can't read your access token from the cookie. HttpOnly cookies are automatically sent in every HTTP request to your server. Thus, leading to very very low chance of a XSS attack.

While if we store our tokens in the form of vanilla javascript variables / local file variables, there is no chance of a XSS attack. Since, this variable value is never exposed. But, the main problem with this approach is that as soon as the user refreshs the page the the variable vanishes and the user is required to sign in again, which is not consisdered as a good software.

** What should we do?

We should store our refresh token in httpOnly enabled cookie while the access token can either be stored as a local variabel and managed through global state management tool like redux or in the local storage itself as this is short life span token.

## Preview

Ignore the UI.

![Http Only Cookie](/markdown/Unauthorised.png)

![Http Only Cookie](/markdown/Login.png)

![Http Only Cookie](/markdown/LoggedIn.png)

> As soon as the user logs in with correct credentionals, a http only generated cookie get's stored in the cookies section.

## Contact

> For any information, feel free to contact with me.
