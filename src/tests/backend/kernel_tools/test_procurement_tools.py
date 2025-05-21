"""Test cases for ProcurementTools class."""
import pytest
from src.backend.kernel_tools.procurement_tools import ProcurementTools


@pytest.mark.asyncio
async def test_order_hardware():
    """Test order_hardware method."""
    result = await ProcurementTools.order_hardware("Laptop", 5)
    assert "Hardware Order Placed" in result
    assert "**Item:** Laptop" in result
    assert "**Quantity:** 5" in result


@pytest.mark.asyncio
async def test_order_software_license():
    """Test order_software_license method."""
    result = await ProcurementTools.order_software_license("Microsoft Office", "Enterprise", 10)
    assert "Software License Ordered" in result
    assert "**Software:** Microsoft Office" in result
    assert "**License Type:** Enterprise" in result
    assert "**Quantity:** 10" in result


@pytest.mark.asyncio
async def test_check_inventory():
    """Test check_inventory method."""
    result = await ProcurementTools.check_inventory("Laptop")
    assert "Inventory Status" in result
    assert "**Item:** Laptop" in result
    assert "**Status:** In Stock" in result


@pytest.mark.asyncio
async def test_process_purchase_order():
    """Test process_purchase_order method."""
    result = await ProcurementTools.process_purchase_order("PO12345")
    assert "Purchase Order Processed" in result
    assert "**PO Number:** PO12345" in result


@pytest.mark.asyncio
async def test_initiate_contract_negotiation():
    """Test initiate_contract_negotiation method."""
    result = await ProcurementTools.initiate_contract_negotiation("Vendor A", "Contract Details")
    assert "Contract Negotiation Initiated" in result
    assert "**Vendor:** Vendor A" in result
    assert "**Contract Details:** Contract Details" in result


@pytest.mark.asyncio
async def test_approve_invoice():
    """Test approve_invoice method."""
    result = await ProcurementTools.approve_invoice("INV12345")
    assert "Invoice Approved" in result
    assert "**Invoice Number:** INV12345" in result


@pytest.mark.asyncio
async def test_track_order():
    """Test track_order method."""
    result = await ProcurementTools.track_order("ORD12345")
    assert "Order Tracking" in result
    assert "**Order Number:** ORD12345" in result
    assert "**Status:** In Transit" in result


@pytest.mark.asyncio
async def test_manage_vendor_relationship():
    """Test manage_vendor_relationship method."""
    result = await ProcurementTools.manage_vendor_relationship("Vendor A", "updated")
    assert "Vendor Relationship Update" in result
    assert "**Vendor:** Vendor A" in result
    assert "**Action:** updated" in result


@pytest.mark.asyncio
async def test_update_procurement_policy():
    """Test update_procurement_policy method."""
    result = await ProcurementTools.update_procurement_policy("Policy A", "New Policy Content")
    assert "Procurement Policy Updated" in result
    assert "**Policy:** Policy A" in result


def test_get_all_kernel_functions():
    """Test get_all_kernel_functions method."""
    kernel_functions = ProcurementTools.get_all_kernel_functions()
    assert "order_hardware" in kernel_functions
    assert "order_software_license" in kernel_functions
    assert callable(kernel_functions["order_hardware"])


def test_generate_tools_json_doc():
    """Test generate_tools_json_doc method."""
    tools_json = ProcurementTools.generate_tools_json_doc()
    assert "order_hardware" in tools_json
    assert "order_software_license" in tools_json
    assert "arguments" in tools_json


@pytest.mark.asyncio
async def test_order_hardware_invalid_quantity():
    """Test order_hardware with invalid quantity."""
    result = await ProcurementTools.order_hardware("Laptop", 0)
    assert "Hardware Order Placed" in result
    assert "**Quantity:** 0" in result


@pytest.mark.asyncio
async def test_order_software_license_invalid_quantity():
    """Test order_software_license with invalid quantity."""
    result = await ProcurementTools.order_software_license("Microsoft Office", "Enterprise", -1)
    assert "Software License Ordered" in result
    assert "**Quantity:** -1" in result


# @pytest.mark.asyncio
# async def test_check_inventory_item_not_found():
#     """Test check_inventory with an item not found."""
#     result = await ProcurementTools.check_inventory("NonExistentItem")
#     assert "Inventory Status" in result
#     assert "**Item:** NonExistentItem" in result
#     assert "**Status:** Not Found" in result


@pytest.mark.asyncio
async def test_process_purchase_order_invalid_po():
    """Test process_purchase_order with an invalid PO number."""
    result = await ProcurementTools.process_purchase_order("")
    assert "Purchase Order Processed" in result
    assert "**PO Number:** " in result


@pytest.mark.asyncio
async def test_initiate_contract_negotiation_empty_details():
    """Test initiate_contract_negotiation with empty contract details."""
    result = await ProcurementTools.initiate_contract_negotiation("Vendor A", "")
    assert "Contract Negotiation Initiated" in result
    assert "**Vendor:** Vendor A" in result
    assert "**Contract Details:** " in result
