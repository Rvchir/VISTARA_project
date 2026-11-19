# VISTARA: Stadium Ticket Booking System
## A Project Report & Synopsis
**Course:** Front End Web Development (26CA205PCB)  
**Academic Session:** 2026–27  
**Department:** Department of Computer Applications, KIET Deemed to be University, Delhi-NCR, Ghaziabad  

---

### Project Team
| Student Name | Roll Number | Email ID |
| :--- | :--- | :--- |
| **Ruchir M Kaushal (Team Leader)** | 2628MCA0131 | 2628mca0131@kiet.edu |
| **Sarvagya Bhardwaj** | 2628MCA0297 | 2628mca0297@kiet.edu |
| **Sarthak Giri** | 2628MCA0251 | 2628mca0251@kiet.edu |

**Under the Supervision of:**  
**Dr. Shashank Bhardwaj**, Associate Professor, Department of Computer Applications  

---

## 1. Abstract
VISTARA is an event ticket booking website created to demonstrate a clear and organised journey for people interested in attending events. The project addresses common difficulties that a prospective spectator may face while looking for match information, comparing seating sections, understanding ticket prices and moving through the booking process. The website brings these activities together in a connected interface.

The current project milestone presents five core linked pages: a home page, a fixtures page, a match booking/details page, a seat selection page and a checkout page, along with interactive confirmation, order tracking, and a procedural 3D stadium preview. The home page introduces the platform and provides navigation. The fixtures page presents match listings with competition filters. The booking page provides match and venue context. The seat selection interface organises seats into blocks and displays seat states such as available, selected and sold. A running summary communicates the selected quantity and displayed amount. The checkout page demonstrates the final step in the customer booking journey.

---

## 2. Motivation & Problem Statement
Booking a ticket for a football match can involve several disconnected steps:
1. Finding the right match among many competitions.
2. Understanding stadium seating arrangements and tiers.
3. Comparing ticket prices across different blocks.
4. Selecting specific seats with clear view angles.

When information is scattered across different platforms or unclear interfaces, the booking process becomes tedious. VISTARA explores how a single, cohesive frontend can streamline event discovery, seating visualization, and checkout demonstration.

---

## 3. Objectives of the Project
- To develop a user-friendly website for football match ticket booking.
- To display upcoming fixtures and important match information in an organised format.
- To provide a clear stadium seating layout for choosing a preferred section and seat.
- To show selected seat details and dynamically calculate the booking amount.
- To create a simple checkout form and a booking confirmation page.
- To provide an order tracking page for demonstrating ticket and booking information.
- To apply semantic HTML5, modern CSS3, and JavaScript/Three.js in a practical frontend application.
- To maintain a clean, modular structure suitable for future backend and payment integrations.

---

## 4. Key Pages & Features

| Page | File | Description |
| :--- | :--- | :--- |
| **Home** | `index.html` | Hero section, interactive SVG seating bowl, competition shortcuts, and search. |
| **Fixtures** | `fixtures.html` | Match listings with filters for ISL, Durand Cup, ACL Two, and dates. |
| **Event Details** | `event.html` | Match overview, stadium details, block selection, and 3-dots action menu with 3D view. |
| **Seat Selection** | `seats.html` | Interactive 6-row seating grid with available, selected, and sold seat indicators. |
| **Checkout** | `checkout.html` | Demonstration checkout form with order summary and ticket delivery choices. |
| **Confirmation** | `confirmation.html` | Matchday ticket stub with QR code placeholder, gate details, and entry code. |
| **Order Tracking** | `track.html` | Order lookup, delivery timeline, ground regulations, and support details. |
| **3D Stadium Preview** | `view3d.html` | Procedural WebGL 3D football stadium built with Three.js for interactive view angle inspection. |

---

## 5. Technology Stack
- **Structure:** Semantic HTML5
- **Styling:** Modern CSS3 (CSS Custom Properties / Tokens, CSS Grid, Flexbox, CSS Counters)
- **3D Graphics:** WebGL via Three.js (Procedural 60,000+ seat stadium geometry)
- **Version Control:** Git & GitHub (`Rvchir/VISTARA_project`)
- **Hosting / Runtime:** Modern Web Browsers (Zero build step, Zero backend dependencies)

---

## 6. Testing & Quality Assurance
- **Page Loading:** Verified that all HTML pages load standalone without runtime errors.
- **Responsive Layouts:** Responsive viewports tested across mobile, tablet, and desktop breakpoints.
- **State Feedback:** Verified visual states for hover, active, selected, and sold seats.
- **Navigation Flow:** Verified uninterrupted end-to-end journey from Fixtures &rarr; Event Details &rarr; Seat Selection &rarr; Checkout &rarr; Confirmation.

---

## 7. Future Scope
1. Connect with backend REST / GraphQL APIs for live match schedules.
2. Real-time seat reservation locking via WebSockets to prevent double-booking.
3. User authentication and customer profile management.
4. Secure payment gateway integration (Razorpay / Stripe).
5. Dynamic PDF ticket generation with signed cryptographic QR codes.
6. Admin dashboard for clubs to manage fixture listings and tier pricing.
