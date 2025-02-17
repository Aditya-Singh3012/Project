# Factory Management System

A comprehensive database management system for factories built with Python and Tkinter. This system helps manage orders, raw materials, stocks, statistics, and undelivered orders through a graphical user interface.

## Features

- **Order Details Management**
  - View all orders
  - Add new orders
  - Remove existing orders
  - Generate QR codes for orders

- **Raw Materials Management**
  - Track raw material inventory
  - Add new materials
  - Remove materials
  - Monitor distributor information
  - Generate QR codes for materials

- **Stock Management**
  - View current stock levels
  - Track quantities and distributors
  - Real-time stock monitoring

- **Statistics Dashboard**
  - View company statistics
  - Track economic metrics
  - Monitor governance factors
  - Compare performance indicators

- **Undelivered Orders Tracking**
  - Monitor pending deliveries
  - Add undelivered orders
  - Remove delivered orders
  - Track order status

## Technical Requirements

- Python 3.x
- Required Libraries:
  - tkinter
  - PIL (Python Imaging Library)
  - mysql.connector
  - qrcode
  - csv

## Database Setup

The system requires a MySQL database named 'factory' with the following tables:
- orderdetails
- rawmaterials
- undelivered

Database Configuration:
- Host: localhost
- User: root
- Password: root
- Database: factory

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install pillow
pip install mysql-connector-python
pip install qrcode
```

3. Set up the MySQL database with the required tables
4. Ensure you have the required image files:
   - laptops.jpg for the main interface
   - test.csv for statistics data

## Usage

1. Run the main script:
```bash
python Factory-Data-Management.py
```

2. Use the main menu to navigate between different modules:
   - Click "Order Details" to manage orders
   - Click "Raw material inputs" to handle inventory
   - Click "Stocks" to view current stock levels
   - Click "Statistics" to view company metrics
   - Click "Undelivered orders" to track pending deliveries

## Data Entry Guidelines

### Adding Orders
- Provide name, quantity, status, client name, and client details
- Ensure all fields are filled correctly
- Status should reflect current order state

### Raw Materials Entry
- Include SNO (Serial Number), name, quantity, distributor, and status
- Maintain consistent unit measurements
- Update status regularly

### Undelivered Orders
- Enter order ID, name, quantity, status, client name, and details
- Keep status updated as delivery progresses
- Remove orders once delivered

## Security Notes

- The system uses default database credentials
- For production use, implement proper security measures
- Regularly backup database data
- Implement user authentication as needed

## Limitations

- Single user system
- Local database only
- Basic security implementation
- Limited to predefined metrics in statistics

## Future Improvements

- Multi-user support
- Cloud database integration
- Enhanced security features
- Advanced analytics
- Mobile application support
- Automated backup system
- Real-time notifications
- Custom report generation

## Support

For issues and feature requests, please contact the development team or create an issue in the repository.
