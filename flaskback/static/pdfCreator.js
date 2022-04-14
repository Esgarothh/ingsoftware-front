var filesLoaded = 0;

var files = {
	img1: {
		url: "https://pbs.twimg.com/profile_images/1083412130307756034/O4c9pith_400x400.jpg",
	},
	img2: {
		url: "https://pbs.twimg.com/profile_images/519367942866104320/PB96rDH_.png",
	},
	img3: {
		url: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqZcRx_cIIQxVkT57vCYx3SGKld2f3mZQvfEEUnP55DU5-mxHH6cSLUcsimncChlBIX_A&usqp=CAU",
	},
};

const invoice = {
	shipping: {
		name: "REsolucion tanto",
		address: "Centro de costos : GERENCIA PERSONAS - Oficina A",
		city: "Asignación anterior:",
		state: "Francisca Gonzales",
		country: "US",
		postal_code: 94111,
	},
	items: [
		{
			item: "100",
			description: "Notebook HP Pavillion 12874x",
			quantity: 2,
			amount: 6000,
		},
		{
			item: "USB_EXT",
			description: "USB Cable Extender",
			quantity: 1,
			amount: 2000,
		},
	],
	subtotal: 8000,
	paid: 0,
	invoice_nr: 1234,
};

function download() {
	if (!blob) return;
	var url = window.URL.createObjectURL(blob);
	a.href = url;
	a.download = "test.pdf";
	a.click();
	window.URL.revokeObjectURL(url);
}
var doc = new PDFDocument({ size: "A4", margin: 50 });

function mostrarpdf() {
	var stream = doc.pipe(blobStream());

	for (var file in files) {
		files[file].xhr = new XMLHttpRequest();
		files[file].xhr.onreadystatechange = function () {
			if (this.readyState == 4 && this.status == 200) {
				loadedFile(this);
			}
		};
		files[file].xhr.responseType = "arraybuffer";
		files[file].xhr.open("GET", files[file].url);
		files[file].xhr.send(null);
	}

	const a = document.createElement("a");
	document.body.appendChild(a);
	a.style = "display: none";

	let blob;

	stream.on("finish", function () {
		// get a blob you can do whatever you like with
		blob = stream.toBlob("application/pdf");

		const url = stream.toBlobURL("application/pdf");
		const iframe = document.querySelector("iframe");
		iframe.src = url;
	});
}

function loadedFile(xhr) {
	for (var file in files) {
		if (files[file].url === xhr.responseURL) {
			files[file].data = xhr.response;
		}
	}
	filesLoaded += 1;
	if (filesLoaded == Object.keys(files).length) {
		showPDF();
	}
}

function showPDF() {
	//generador INSIDE

	generateHeader(doc);
	generateCustomerInformation(doc, invoice);
	generateInvoiceTable(doc, invoice);
	generateFooter(doc);

	doc.end();
}
// ---------------------------------------------------------------------------------- FUNCIONES

function generateHeader(doc) {
	doc

		.fillColor("#444444")
		.fontSize(20)
		.text("Pizarras Grecia", 110, 57)
		.fontSize(10)
		.text("Manufacturas Grecia.", 200, 50, { align: "right" })
		.text("Sierra Bella 2667", 200, 65, { align: "right" })
		.text("Santiago de Chile", 200, 80, { align: "right" })
		.moveDown();
}

function generateCustomerInformation(doc, invoice) {
	doc.fillColor("#444444").fontSize(20).text("Factura", 50, 160);

	generateHr(doc, 185);

	const customerInformationTop = 200;

	doc
		.fontSize(10)
		.text("N° Factura:", 50, customerInformationTop)
		.font("Helvetica-Bold")
		.text(invoice.invoice_nr, 150, customerInformationTop)
		.font("Helvetica")
		.text("Fecha:", 50, customerInformationTop + 15)
		.text(formatDate(new Date()), 150, customerInformationTop + 15)
		.text("Monto Total:", 50, customerInformationTop + 30)
		.text(
			formatCurrency(invoice.subtotal - invoice.paid),
			150,
			customerInformationTop + 30
		)

		.font("Helvetica-Bold")
		.text(invoice.shipping.name, 300, customerInformationTop)
		.font("Helvetica")
		.text(invoice.shipping.address, 300, customerInformationTop + 15)
		.text(
			invoice.shipping.city +
				", " +
				invoice.shipping.state +
				", " +
				invoice.shipping.country,
			300,
			customerInformationTop + 30
		)
		.moveDown();

	generateHr(doc, 252);
}

function generateInvoiceTable(doc, invoice) {
	let i;
	const invoiceTableTop = 330;

	doc.font("Helvetica-Bold");
	generateTableRow(
		doc,
		invoiceTableTop,
		"Producto",
		"Descripcion",
		"Costo Unitario",
		"Cantidad",
		"Total"
	);
	generateHr(doc, invoiceTableTop + 20);
	doc.font("Helvetica");

	for (i = 0; i < invoice.items.length; i++) {
		const item = invoice.items[i];
		const position = invoiceTableTop + (i + 1) * 30;
		generateTableRow(
			doc,
			position,
			item.item,
			item.description,
			formatCurrency(item.amount / item.quantity),
			item.quantity,
			formatCurrency(item.amount)
		);

		generateHr(doc, position + 20);
	}

	const subtotalPosition = invoiceTableTop + (i + 1) * 30;
	generateTableRow(
		doc,
		subtotalPosition,
		"",
		"",
		"Neto",
		"",
		formatCurrency(invoice.subtotal)
	);

	const paidToDatePosition = subtotalPosition + 20;
	generateTableRow(
		doc,
		paidToDatePosition,
		"",
		"",
		"IVA",
		"",
		formatCurrency(invoice.paid)
	);

	const duePosition = paidToDatePosition + 25;
	doc.font("Helvetica-Bold");
	generateTableRow(
		doc,
		duePosition,
		"",
		"",
		"Total",
		"",
		formatCurrency(invoice.subtotal - invoice.paid)
	);
	doc.font("Helvetica");
}

function generateFooter(doc) {
	doc
		.fontSize(10)
		.text(
			"Payment is due within 15 days. Thank you for your business.",
			50,
			780,
			{ align: "center", width: 500 }
		);
}

function generateTableRow(
	doc,
	y,
	item,
	description,
	unitCost,
	quantity,
	lineTotal
) {
	doc
		.fontSize(10)
		.text(item, 50, y)
		.text(description, 150, y)
		.text(unitCost, 280, y, { width: 90, align: "right" })
		.text(quantity, 370, y, { width: 90, align: "right" })
		.text(lineTotal, 0, y, { align: "right" });
}

function generateHr(doc, y) {
	doc.strokeColor("#aaaaaa").lineWidth(1).moveTo(50, y).lineTo(550, y).stroke();
}

function formatCurrency(cents) {
	return "$" + (cents / 100).toFixed(2);
}

function formatDate(date) {
	const day = date.getDate();
	const month = date.getMonth() + 1;
	const year = date.getFullYear();

	return year + "/" + month + "/" + day;
}
