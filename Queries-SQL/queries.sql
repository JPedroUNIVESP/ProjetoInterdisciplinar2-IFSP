-- Checando os dados. Há duplicados? se sim, quantas linhas duplicadas?
SELECT
    COUNT(*) AS total_duplicatas
FROM
    (
    SELECT
        price,
        condo,
        size,
        rooms,
        toilets,
        suites,
        parking,
        elevator,
        furnished,
        swimming_pool,
        new, district,
        negotiation_type,
        property_type,
        latitude,
        longitude,
        COUNT(*) AS count_duplicatas
    FROM
        raw
    GROUP BY
        price, condo, size, rooms, toilets, suites, parking, elevator, furnished, swimming_pool, new, district,
        negotiation_type, property_type, latitude, longitude
    HAVING
        COUNT(*) > 1
    ) AS duplicatas;


-- Calculando a média de preços (em cima da base sem dados duplicados), considerando o tipo de negociação: Aluguel ou Venda
SELECT
    negotiation_type,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS count_properties
FROM
    (SELECT DISTINCT * FROM raw)
GROUP BY negotiation_type;


-- Cálculo da média do preço de aluguel e venda, por distrito
SELECT
    district,
    AVG(CASE WHEN negotiation_type = 'rent' THEN price END) AS avg_rent_price,
    AVG(CASE WHEN negotiation_type = 'sale' THEN price END) AS avg_sale_price
FROM
    raw
GROUP BY
    district
ORDER BY
    district;


-- Contagem de imóveis com/sem elevador e com/sem piscina, para aluguel e venda
SELECT
    negotiation_type,
    elevator,
    swimming_pool,
    COUNT(*) AS count_properties
FROM
    raw
GROUP BY
    negotiation_type, elevator, swimming_pool
ORDER BY negotiation_type;


-- Distribuição de tipos de propriedades para aluguel e venda:
SELECT
    negotiation_type,
    property_type,
    COUNT(*) AS count_properties
FROM
    raw
GROUP BY
    negotiation_type, property_type;


-- Média do tamanho dos imóveis, por tipo de propriedade, para aluguel e venda:
SELECT
    negotiation_type,
    property_type,
    ROUND(AVG(size), 2) AS avg_size
FROM
    raw
GROUP BY
    negotiation_type, property_type
ORDER BY
    negotiation_type, avg_size DESC;


-- Proporção de propriedades com/sem mobílias para aluguel e venda:
SELECT
    negotiation_type,
    furnished,
    COUNT(*) AS count_properties
FROM
    raw
GROUP BY
    negotiation_type, furnished
ORDER BY negotiation_type;

-- Verificação de imóveis com o mesmo preço, porém um para locação e outro para venda.
--(Esses casos podem ser sujeira na base)
SELECT
    a.price AS aluguel_price,
    a.size AS aluguel_size,
    a.rooms AS aluguel_rooms,
    a.toilets AS aluguel_toilets,
    a.suites AS aluguel_suites,
    a.parking AS aluguel_parking,
    a.district_zone AS aluguel_district_zone,
    a.property_type AS aluguel_property_type,
    v.price AS venda_price,
    v.size AS venda_size,
    v.rooms AS venda_rooms,
    v.toilets AS venda_toilets,
    v.suites AS venda_suites,
    v.parking AS venda_parking,
    v.district_zone AS venda_district_zone,
    v.property_type AS venda_property_type
FROM
    aluguel a
INNER JOIN
    venda v ON a.price = v.price;

-- Análise estatística da distribuição dos preços de venda na base de dados, agrupando as propriedades em diferentes
-- faixas de preços e contabilizando os valores.
SELECT
    price_range,
    COUNT(*) AS count_properties
FROM (SELECT
        CASE
            WHEN price BETWEEN 0 AND 500000 THEN '0-500K'
            WHEN price BETWEEN 500001 AND 1000000 THEN '500K-1M'
            WHEN price BETWEEN 1000001 AND 1500000 THEN '1M-1.5M'
            WHEN price BETWEEN 1500001 AND 2000000 THEN '1.5M-2M'
            ELSE '2M ou mais'
        END AS price_range,
        CASE
            WHEN price BETWEEN 0 AND 500000 THEN 1
            WHEN price BETWEEN 500001 AND 1000000 THEN 2
            WHEN price BETWEEN 1000001 AND 1500000 THEN 3
            WHEN price BETWEEN 1500001 AND 2000000 THEN 4
            ELSE 5
        END AS id
    FROM
        venda)
GROUP BY
    id, price_range
ORDER BY
    id;

-- Análise estatística da distribuição dos preços de aluguel na base de dados, agrupando as propriedades em diferentes
-- faixas de preços e contabilizando os valores.
SELECT
    price_range,
    COUNT(*) AS count_properties
FROM (SELECT
        CASE
            WHEN price BETWEEN 0 AND 1000 THEN '0-1K'
            WHEN price BETWEEN 1001 AND 2000 THEN '1K-2K'
            WHEN price BETWEEN 2001 AND 3000 THEN '2K-3K'
            WHEN price BETWEEN 3001 AND 4000 THEN '3K-4K'
            ELSE '4K ou mais'
        END AS price_range,
        CASE
            WHEN price BETWEEN 0 AND 1000 THEN 1
            WHEN price BETWEEN 1001 AND 2000 THEN 2
            WHEN price BETWEEN 2001 AND 3000 THEN 3
            WHEN price BETWEEN 3001 AND 4000 THEN 4
            ELSE 5
        END AS id
    FROM
        aluguel)
GROUP BY
    id, price_range
ORDER BY
    id;