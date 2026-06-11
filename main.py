from database import (
    initialize_db, add_record, view_all,
    search_record, update_record, delete_record
)

# ─── Display a single record ───────────────────────────────────
def print_record(r):
    print("-" * 45)
    print(f"  ID           : {r['id']}")
    print(f"  Amount       : {r['amount']}")
    print(f"  Category     : {r['category']}")
    print(f"  Description  : {r['description']}")
    print(f"  Expense Date : {r['expense_date']}")
    print("-" * 45)

# ─── Main Menu ─────────────────────────────────────────────────
def menu():
    print("\n========================================")
    print("        🗂️  My Mini Project")
    print("========================================")
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Search Expense")
    print("  4. Update Expense")
    print("  5. Delete Expense")
    print("  6. Exit")
    print("========================================")

# ─── Main Program ──────────────────────────────────────────────
def main():
    initialize_db()

    while True:
        menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Add New Record ---")
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ").strip()
            description = input("Enter Description: ").strip()
            expense_date = input("Enter Date (YYYY-MM-DD): ").strip()

            add_record(amount, category, description, expense_date)

        elif choice == "2":
            print("\n--- All Records ---")
            records = view_all()
            if records:
                for r in records:
                    print_record(r)
            else:
                print("No records found.")

        elif choice == "3":
            keyword = input("\nEnter category or description to search: ").strip()
            results = search_record(keyword)
            if results:
                for r in results:
                    print_record(r)
            else:
                print("No matching records found.")

        elif choice == "4":
            rid = input("\nEnter Record ID to update: ").strip()
            amount = float(input("New Amount: "))
            category = input("New Category: ").strip()
            description = input("New Description: ").strip()
            expense_date = input("New Date (YYYY-MM-DD): ").strip()

            update_record(
                int(rid),
                amount,
                category,
                description,
                expense_date
            )

        elif choice == "5":
            rid = input("\nEnter Record ID to delete: ").strip()
            confirm = input(f"Delete record {rid}? (yes/no): ").strip().lower()
            if confirm == "yes":
                delete_record(int(rid))
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()