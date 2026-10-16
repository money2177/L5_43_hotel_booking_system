"""Hotel room reservation and booking management module."""

import hashlib
import secrets
from pathlib import Path

room_inventory = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Reserve an available room and record the booking."""
    if room_num not in room_inventory or room_inventory[room_num]["is_booked"]:
        return False

    if booking_log is None:
        booking_log = []

    room_inventory[room_num]["is_booked"] = True
    booking_log.append(f"Reserved room {room_num} for guest {guest_name}")
    return True


def cancel_booking(room_num):
    """Cancel a booking if the room exists and is currently booked."""
    room = room_inventory.get(room_num)

    if room is None or not room["is_booked"]:
        return False

    room["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return True if the specified room is available."""
    room = room_inventory.get(room_num)
    return room is not None and not room["is_booked"]


def compute_seasonal_rate(room_num, multiplier=1.25):
    """Calculate the seasonal room rate using a numeric multiplier."""
    room = room_inventory.get(room_num)

    if room is None:
        raise ValueError(f"Unknown room number: {room_num}")

    if (
        isinstance(multiplier, bool)
        or not isinstance(multiplier, (int, float))
        or multiplier <= 0
    ):
        raise ValueError("Multiplier must be a positive number.")

    return round(room["price"] * multiplier, 2)


def generate_guest_hash(guest_id):
    """Generate a SHA-256 digest for a guest identifier."""
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref():
    """Generate an unpredictable booking reference."""
    return secrets.token_hex(4).upper()


def export_room_ledger(filename="hotel_ledger.txt"):
    """Export the room inventory to a UTF-8 text file."""
    output_path = Path(filename)

    ledger = "\n".join(
        f"{number}: {room['type']}, "
        f"price={room['price']:.2f}, "
        f"booked={room['is_booked']}"
        for number, room in sorted(room_inventory.items())
    )

    output_path.write_text(ledger + "\n", encoding="utf-8")
    print(f"Hotel ledger exported to: {output_path}")


def main():
    """Demonstrate the hotel booking system."""
    booking_log = []

    book_room("101", "Example Guest", booking_log)
    cancel_booking("102")

    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())
    print("Booking log:", booking_log)

    export_room_ledger()


if __name__ == "__main__":
    main()
