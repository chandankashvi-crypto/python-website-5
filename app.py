# =====================================================
# StayEase - Hotel Booking Cost Calculator (website version)
# College project: Python Programming for Business Students
#  This is a cost estimator, not a real booking system.
# Colour scheme: blue, gold and white
# =====================================================

import streamlit as st

st.set_page_config(page_title="StayEase", page_icon="🏨", layout="wide",
                   initial_sidebar_state="expanded")

# ---------------------------------------------------------------
# Styling (CSS). 
# Colours: blue #0B2A5B, gold #D4AF37, white
# ---------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&display=swap');

/* ---------- Whole page: blue background ---------- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #061A3F 0%, #0B3C8C 60%, #14509F 100%); }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] * { color: #FFFFFF !important; }
.block-container { padding-top: 4rem; max-width: 1150px; }

/* ---------- Sidebar (side menu) ---------- */
[data-testid="stSidebar"] { background: #061A3F; border-right: 2px solid #D4AF37; }
[data-testid="stSidebar"] * { color: #FFFFFF; }
[data-testid="stSidebarCollapseButton"] *, [data-testid="stExpandSidebarButton"] * { color: #FFFFFF !important; }
.side-brand { background: linear-gradient(135deg, #0B3C8C, #14509F); padding: 1.1rem 1.2rem;
              border-bottom: 3px solid #D4AF37; border-radius: 6px; margin-bottom: 1rem; }
.side-brand-name { font-family: 'Playfair Display', Georgia, serif; font-size: 1.7rem; color: #FFFFFF !important; }
.side-brand-tag { color: #D4AF37 !important; font-size: 0.95rem; }
[data-testid="stSidebar"] [role="radiogroup"] label { padding: 0.6rem 0.8rem; border-left: 3px solid transparent;
              border-radius: 4px; width: 100%; }
[data-testid="stSidebar"] [role="radiogroup"] label > div > div:first-child { display: none; }
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
              background: rgba(212, 175, 55, 0.15); border-left-color: #D4AF37; }
[data-testid="stSidebar"] [role="radiogroup"] label p { font-weight: 600; font-size: 1.05rem; }
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] * { color: #C9D6EE !important; opacity: 1 !important; }
.side-rates { border: 1px solid #D4AF37; border-radius: 6px; padding: 0.9rem 1rem; margin-top: 1.2rem; }
.side-rates-title { color: #D4AF37 !important; letter-spacing: 2px; font-size: 0.8rem; font-weight: 700; margin-bottom: 0.4rem; }
.side-row { display: flex; justify-content: space-between; padding: 0.25rem 0; font-size: 0.95rem; }
.side-price { color: #D4AF37 !important; font-weight: 700; }

/* ---------- Text blocks on the blue background ---------- */
.hero-label { color: #D4AF37; letter-spacing: 4px; font-weight: 600; font-size: 0.85rem; }
.hero-title { font-family: 'Playfair Display', Georgia, serif; color: #FFFFFF;
              font-size: 3.4rem; line-height: 1.15; margin: 0.6rem 0 1rem 0; }
.page-title { font-family: 'Playfair Display', Georgia, serif; color: #FFFFFF;
              font-size: 2.6rem; line-height: 1.2; margin: 0.4rem 0 0.8rem 0; }
.hero-text { color: #EAF0FA; font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.2rem; }
.hero-link { display: inline-block; color: #FFFFFF; letter-spacing: 3px; font-weight: 600;
             border-bottom: 2px solid #D4AF37; padding-bottom: 4px; margin: 0.8rem 0 1.5rem 0; }
.hero-note { color: #C9D6EE; font-size: 0.85rem; font-style: italic; margin-bottom: 1.2rem; }
.footer-note { color: #C9D6EE; font-size: 0.8rem; text-align: center; margin-top: 3rem;
               border-top: 1px solid rgba(212, 175, 55, 0.4); padding-top: 1rem; }

/* ---------- White cards ---------- */
.white-card, .st-key-booking_card { background: #FFFFFF; padding: 2rem; border-radius: 6px;
                       box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35); }
.card-title { font-family: 'Playfair Display', Georgia, serif; color: #0B2A5B;
              font-size: 2rem; margin-bottom: 0.5rem; }
.rate-row { display: flex; justify-content: space-between; color: #0B2A5B;
            padding: 0.7rem 0; border-bottom: 1px solid #E3E8F2; }
.rate-price { color: #B8902B; font-weight: 700; }
.card-note { color: #5A6B8C; font-size: 0.85rem; margin-top: 0.9rem; }
.room-name { font-family: 'Playfair Display', Georgia, serif; color: #0B2A5B; font-size: 1.5rem; }
.room-price { color: #B8902B; font-size: 2.1rem; font-weight: 700; margin-top: 0.4rem; }
.room-unit { color: #5A6B8C; font-size: 0.85rem; margin-bottom: 0.8rem; }
.room-facilities { color: #0B2A5B; font-size: 0.95rem; line-height: 1.7; }

/* ---------- Gold-bordered glass cards ---------- */
.glass-card, .st-key-result_card { background: rgba(255, 255, 255, 0.08); border: 1px solid #D4AF37;
                      border-radius: 6px; padding: 1.5rem; }
.glass-title, .result-title { font-family: 'Playfair Display', Georgia, serif; color: #D4AF37;
                font-size: 1.6rem; margin-bottom: 0.6rem; }
.glass-text { color: #FFFFFF; line-height: 1.7; }
.step-number { color: #D4AF37; font-size: 2rem; font-weight: 700; font-family: 'Playfair Display', Georgia, serif; }
.bill-row { display: flex; justify-content: space-between; color: #FFFFFF;
            padding: 0.55rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.18); }
.bill-gold { color: #D4AF37; font-weight: 600; }
.saved-note { color: #D4AF37; font-weight: 600; margin-top: 0.6rem; }

/* ---------- Booking form inputs (light boxes, even in dark mode) ---------- */
.st-key-booking_card label p { color: #0B2A5B !important; font-weight: 500; }
.st-key-booking_card [data-testid="stSelectbox"] div,
.st-key-booking_card [data-testid="stNumberInputContainer"],
.st-key-booking_card [data-testid="stNumberInputContainer"] div {
    background-color: #F4F6FB !important; color: #0B2A5B !important; }
.st-key-booking_card [data-testid="stWidgetLabel"],
.st-key-booking_card [data-testid="stWidgetLabel"] div { background-color: transparent !important; }
.st-key-booking_card input, .st-key-booking_card [data-testid="stSelectbox"] * { color: #0B2A5B !important; }
.st-key-booking_card [data-testid="stNumberInputContainer"] button { color: #0B2A5B !important; }
.st-key-booking_card [data-testid="stCheckbox"] label > div:first-of-type {
    background-color: #FFFFFF !important; border: 1.5px solid #0B2A5B !important; }
.st-key-booking_card [data-testid="stCheckbox"] label:has(input:checked) > div:first-of-type {
    background-color: #D4AF37 !important; border-color: #D4AF37 !important; }
[data-testid="stSelectboxVirtualDropdown"], [data-testid="stSelectboxVirtualDropdown"] * ,
ul[role="listbox"], ul[role="listbox"] li { background-color: #FFFFFF !important; color: #0B2A5B !important; }

/* ---------- Final total (gold bar) and gold buttons ---------- */
.st-key-total_box [data-testid="stAlert"] { background-color: #D4AF37 !important; border-radius: 4px; margin-top: 1rem; }
.st-key-total_box [data-testid="stAlert"] * { color: #061A3F !important; font-weight: 700;
            background-color: transparent !important; }
.st-key-save_button button, .st-key-clear_button button { background-color: #D4AF37 !important;
            border: none !important; border-radius: 4px; }
.st-key-save_button button *, .st-key-clear_button button * { color: #061A3F !important; font-weight: 700; }

/* ---------- Bookings table ---------- */
[data-testid="stTable"] table { background: transparent; border-collapse: collapse; width: 100%; }
[data-testid="stTable"] th { color: #D4AF37 !important; background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(212, 175, 55, 0.5) !important; }
[data-testid="stTable"] td { color: #FFFFFF !important; background: transparent !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Data: prices, facilities and rules (all in rupees, all sample values).
# Everything that appears on screen is built from these variables,
# so changing a value here updates every page.
# ---------------------------------------------------------------
room_prices = {
    "Standard Room": 2500,
    "Deluxe Room": 4000,
    "Suite": 6500
}

room_facilities = {
    "Standard Room": "Queen bed • Free Wi-Fi • Air conditioning • Smart TV",
    "Deluxe Room": "King bed • City view • Mini bar • Work desk • Free Wi-Fi",
    "Suite": "King bed • Private lounge • Bathtub • Balcony • Free Wi-Fi"
}

breakfast_price = 500      # per guest, per night
extra_bed_price = 1000     # per night
late_checkout_price = 500  # once per booking

MIN_NIGHTS, MAX_NIGHTS = 1, 30
MIN_GUESTS, MAX_GUESTS = 1, 10

SHORT_STAY_NIGHTS = 3      # from this many nights, the short-stay discount applies
LONG_STAY_NIGHTS = 5       # from this many nights, the long-stay discount applies
SHORT_STAY_DISCOUNT = 5    # percent
LONG_STAY_DISCOUNT = 10    # percent


# ---------------------------------------------------------------
# Functions
# ---------------------------------------------------------------
def calculate_discount(nights):
    """Return the discount percentage for a stay of the given number of nights."""
    if nights >= LONG_STAY_NIGHTS:
        return LONG_STAY_DISCOUNT
    elif nights >= SHORT_STAY_NIGHTS:
        return SHORT_STAY_DISCOUNT
    else:
        return 0


def is_valid_booking(nights, guests):
    """Backup check. The input boxes already limit the values, but this keeps
    the calculation safe if those limits are ever changed or removed."""
    return MIN_NIGHTS <= nights <= MAX_NIGHTS and MIN_GUESTS <= guests <= MAX_GUESTS


def yes_no(ticked):
    """Convert a checkbox value (True/False) into the text shown in the table."""
    if ticked:
        return "Yes"
    return "No"


# Session memory: st.session_state keeps saved bookings while the site is open
if "bookings" not in st.session_state:
    st.session_state["bookings"] = []

# ---------------------------------------------------------------
# Sidebar menu
# ---------------------------------------------------------------
with st.sidebar:
    st.markdown("""
<div class="side-brand">
<div class="side-brand-name">🏨 StayEase</div>
<div class="side-brand-tag">Your stay, your way.</div>
</div>
""", unsafe_allow_html=True)

    page = st.radio(
        "Menu",
        ["Home", "Browse Rooms", "Book a Room", "My Bookings", "About / Contact"],
        captions=[
            "Welcome page and hotel introduction.",
            "View room types, prices and facilities.",
            "Enter nights, guests and extras.",
            "View bookings saved during this session.",
            "Hotel information and contact details."
        ],
        label_visibility="collapsed"
    )

    # Build one sidebar row per room type
    sidebar_rows = ""
    for room_name, price in room_prices.items():
        sidebar_rows += f'<div class="side-row"><span>{room_name}</span><span class="side-price">₹{price:,}</span></div>\n'

    st.markdown(f"""
<div class="side-rates">
<div class="side-rates-title">ROOM RATES (PER NIGHT)</div>
{sidebar_rows}</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Pages (if / elif / else shows ONE page)
# ---------------------------------------------------------------
if page == "Home":
    home_left, home_right = st.columns([1.3, 1], gap="large")

    with home_left:
        st.markdown("""
<div class="hero-label">HOTEL COST CALCULATOR</div>
<div class="hero-title">StayEase<br>Plan Your Stay, Know Your Price</div>
<div class="hero-text">Choose your room and extras to estimate the cost of your stay. Longer stays unlock bigger discounts.</div>
<div class="hero-link">WELCOME TO STAYEASE</div>
<div class="hero-note">Note: All prices and discounts shown here are sample assumptions for a college project.</div>
""", unsafe_allow_html=True)

    with home_right:
        rate_rows = ""
        for room_name, price in room_prices.items():
            rate_rows += f'<div class="rate-row"><span>{room_name}</span><span class="rate-price">₹{price:,} / night</span></div>\n'

        st.markdown(f"""
<div class="white-card">
<div class="card-title">Rooms &amp; Rates</div>
{rate_rows}<div class="card-note">Open "Book a Room" from the menu to estimate your total cost.</div>
</div>
""", unsafe_allow_html=True)

    step_1, step_2, step_3 = st.columns(3, gap="large")
    with step_1:
        st.markdown("""
<div class="glass-card"><div class="step-number">1</div><div class="glass-title">Choose</div>
<div class="glass-text">Pick a room type, the number of nights and the number of guests.</div></div>
""", unsafe_allow_html=True)
    with step_2:
        st.markdown("""
<div class="glass-card"><div class="step-number">2</div><div class="glass-title">Customise</div>
<div class="glass-text">Add breakfast, an extra bed or late checkout if you need them.</div></div>
""", unsafe_allow_html=True)
    with step_3:
        st.markdown("""
<div class="glass-card"><div class="step-number">3</div><div class="glass-title">See Your Price</div>
<div class="glass-text">Get an itemised bill with your discount and final total instantly.</div></div>
""", unsafe_allow_html=True)

elif page == "Browse Rooms":
    st.markdown("""
<div class="hero-label">OUR ROOMS</div>
<div class="page-title">Rooms, Prices and Facilities</div>
<div class="hero-text">Every price below is per room, per night.</div>
""", unsafe_allow_html=True)

    # One card per room type, created with a loop instead of repeating the same block
    room_columns = st.columns(len(room_prices), gap="large")
    for column, room_name in zip(room_columns, room_prices):
        with column:
            st.markdown(f"""
<div class="white-card"><div class="room-name">{room_name}</div>
<div class="room-price">₹{room_prices[room_name]:,}</div><div class="room-unit">per night</div>
<div class="room-facilities">{room_facilities[room_name]}</div></div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    extras_column, discount_column = st.columns(2, gap="large")
    with extras_column:
        st.markdown(f"""
<div class="glass-card"><div class="glass-title">Extra Services</div>
<div class="bill-row"><span>Breakfast (per guest, per night)</span><span>₹{breakfast_price:,}</span></div>
<div class="bill-row"><span>Extra bed (per night)</span><span>₹{extra_bed_price:,}</span></div>
<div class="bill-row"><span>Late checkout (once per booking)</span><span>₹{late_checkout_price:,}</span></div></div>
""", unsafe_allow_html=True)
    with discount_column:
        st.markdown(f"""
<div class="glass-card"><div class="glass-title">Stay Discounts</div>
<div class="bill-row"><span>{MIN_NIGHTS} - {SHORT_STAY_NIGHTS - 1} nights</span><span>No discount</span></div>
<div class="bill-row"><span>{SHORT_STAY_NIGHTS} - {LONG_STAY_NIGHTS - 1} nights</span><span class="bill-gold">{SHORT_STAY_DISCOUNT}% off</span></div>
<div class="bill-row"><span>{LONG_STAY_NIGHTS} - {MAX_NIGHTS} nights</span><span class="bill-gold">{LONG_STAY_DISCOUNT}% off</span></div></div>
""", unsafe_allow_html=True)

elif page == "Book a Room":
    # Left column shows the results, right column holds the booking form
    left_column, right_column = st.columns([1.3, 1], gap="large")

    with right_column:
        with st.container(key="booking_card"):
            st.markdown('<div class="card-title">Estimate Your Stay</div>', unsafe_allow_html=True)

            room_type = st.selectbox("Room type", list(room_prices.keys()))
            nights = st.number_input(f"Number of nights ({MIN_NIGHTS} to {MAX_NIGHTS})",
                                     min_value=MIN_NIGHTS, max_value=MAX_NIGHTS, value=MIN_NIGHTS, step=1)
            guests = st.number_input(f"Number of guests ({MIN_GUESTS} to {MAX_GUESTS})",
                                     min_value=MIN_GUESTS, max_value=MAX_GUESTS, value=MIN_GUESTS, step=1)

            # Checkbox labels use the price variables so they never go out of date
            want_breakfast = st.checkbox(f"Breakfast (₹{breakfast_price:,} per guest per night)")
            want_extra_bed = st.checkbox(f"Extra bed (₹{extra_bed_price:,} per night)")
            want_late_checkout = st.checkbox(f"Late checkout (₹{late_checkout_price:,} once per booking)")

    with left_column:
        st.markdown("""
<div class="hero-label">BOOK A ROOM</div>
<div class="page-title">Your Stay, Calculated</div>
<div class="hero-note">Note: All prices and discounts shown here are sample assumptions for a college project.</div>
""", unsafe_allow_html=True)

        with st.container(key="result_card"):
            if not is_valid_booking(nights, guests):
                st.error(f"Nights must be {MIN_NIGHTS}-{MAX_NIGHTS} and guests must be {MIN_GUESTS}-{MAX_GUESTS}.")
            else:
                # Room cost = price per night x number of nights
                room_price_per_night = room_prices[room_type]
                room_cost = room_price_per_night * nights

                # Optional services cost 0 unless ticked
                breakfast_cost = 0
                extra_bed_cost = 0
                late_checkout_cost = 0

                if want_breakfast:
                    breakfast_cost = breakfast_price * guests * nights  # per guest AND per night
                if want_extra_bed:
                    extra_bed_cost = extra_bed_price * nights           # per night only
                if want_late_checkout:
                    late_checkout_cost = late_checkout_price            # charged once

                services_cost = breakfast_cost + extra_bed_cost + late_checkout_cost

                # The discount applies to room cost plus services
                subtotal = room_cost + services_cost
                discount_percent = calculate_discount(nights)
                discount_amount = subtotal * discount_percent / 100
                final_total = subtotal - discount_amount

                st.markdown(f"""
<div class="result-title">Your Price Breakdown</div>
<div class="bill-row"><span>Room: {room_type} - ₹{room_price_per_night:,.2f} x {nights} night(s)</span><span>₹{room_cost:,.2f}</span></div>
<div class="bill-row"><span>Breakfast</span><span>₹{breakfast_cost:,.2f}</span></div>
<div class="bill-row"><span>Extra bed</span><span>₹{extra_bed_cost:,.2f}</span></div>
<div class="bill-row"><span>Late checkout</span><span>₹{late_checkout_cost:,.2f}</span></div>
<div class="bill-row"><span>Subtotal</span><span>₹{subtotal:,.2f}</span></div>
<div class="bill-row bill-gold"><span>Discount ({discount_percent}%)</span><span>- ₹{discount_amount:,.2f}</span></div>
""", unsafe_allow_html=True)
                with st.container(key="total_box"):
                    st.success(f"Final Total: ₹{final_total:,.2f}")

                if st.button("Save to My Bookings", key="save_button"):
                    st.session_state["bookings"].append({
                        "Room": room_type,
                        "Nights": nights,
                        "Guests": guests,
                        "Breakfast": yes_no(want_breakfast),
                        "Extra bed": yes_no(want_extra_bed),
                        "Late checkout": yes_no(want_late_checkout),
                        "Discount": f"{discount_percent}%",
                        "Final total": f"₹{final_total:,.2f}"
                    })
                    st.markdown('<div class="saved-note">✓ Saved. Open "My Bookings" from the menu to see it.</div>',
                                unsafe_allow_html=True)

elif page == "My Bookings":
    st.markdown("""
<div class="hero-label">MY BOOKINGS</div>
<div class="page-title">Saved During This Session</div>
<div class="hero-text">These are estimates you saved. They are not real reservations and disappear when the page is refreshed.</div>
""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if len(st.session_state["bookings"]) == 0:
        st.info("You have no saved bookings yet. Go to 'Book a Room', then press 'Save to My Bookings'.")
    else:
        st.table(st.session_state["bookings"])
        if st.button("Clear all bookings", key="clear_button"):
            st.session_state["bookings"] = []
            st.rerun()  # refresh so the table disappears

else:
    st.markdown("""
<div class="hero-label">ABOUT / CONTACT</div>
<div class="page-title">About StayEase</div>
""", unsafe_allow_html=True)

    about_column, contact_column = st.columns([1.3, 1], gap="large")
    with about_column:
        st.markdown("""
<div class="glass-card"><div class="glass-title">Our Story</div>
<div class="glass-text">StayEase is a sample hotel cost calculator built as a college project for
Python Programming for Business Students. It helps a customer estimate the price of a stay
before booking, with clear room rates, optional services and length-of-stay discounts.<br><br>
It is not a real reservation system. All prices, facilities and policies are sample assumptions.</div></div>
""", unsafe_allow_html=True)
    with contact_column:
        st.markdown("""
<div class="white-card"><div class="card-title">Contact Us</div>
<div class="rate-row"><span>Email</span><span class="rate-price">hello@stayease.example</span></div>
<div class="rate-row"><span>Phone</span><span class="rate-price">+91 00000 00000</span></div>
<div class="rate-row"><span>Front desk</span><span class="rate-price">Open 24 hours</span></div>
<div class="card-note">Sample contact details for a college project.</div></div>
""", unsafe_allow_html=True)
