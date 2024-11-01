import xlwings as xw
import time

# Define the file path to your Excel file
file_path = r"C:\Users\Junaid Javed\Downloads\test_auto_refresh.xlsx"

# Start an Excel application in the foreground (visible to the user)
app = xw.App(visible=True)

try:
    # Open the specified workbook
    wb = app.books.open(file_path)

    # Refresh all data connections in the workbook
    wb.api.RefreshAll()

    # Allow time for the refresh to complete
    time.sleep(5)

    # Check if refresh was successful
    for sheet in wb.sheets:
        print(f"Refreshing sheet: {sheet.name}")

    # Save the changes made to the workbook
    wb.save()

    print("Workbook refreshed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the workbook
    wb.close()
    # Quit the Excel application
    app.quit()
